"""Install verified MSYS2 native DLLs into this project's Windows virtualenv.

Run with .venv\Scripts\python.exe. No administrator installer is required.
Only runtime DLLs, supporting data, and licenses are extracted; Python packages
and executables from MSYS2 are not installed into the interpreter.
"""

import hashlib
import io
import json
import os
import re
import sys
import tarfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath
from xml.sax.saxutils import escape

import requests
import zstandard


BASE = "https://repo.msys2.org/mingw/ucrt64/"
ROOT_PACKAGE = "mingw-w64-ucrt-x86_64-pango"


def get_bytes(url):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=(15, 60))
            response.raise_for_status()
            return response.content
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


def read_database():
    data = get_bytes(BASE + "ucrt64.db")
    if data.startswith(b"\x28\xb5\x2f\xfd"):
        with zstandard.ZstdDecompressor().stream_reader(io.BytesIO(data)) as reader:
            data = reader.read()
    packages = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as archive:
        for member in archive:
            if not member.name.endswith("/desc"):
                continue
            fields, key = {}, None
            for line in archive.extractfile(member).read().decode("utf-8").splitlines():
                if line.startswith("%") and line.endswith("%"):
                    key = line.strip("%")
                    fields[key] = []
                elif line and key:
                    fields[key].append(line)
            packages[fields["NAME"][0]] = fields
    return packages


def dependency_closure(packages):
    strip_version = lambda value: re.split("[<>=]", value, maxsplit=1)[0]
    providers = {
        strip_version(item): name
        for name, fields in packages.items()
        for item in fields.get("PROVIDES", [])
    }
    selected = set()

    def visit(name):
        name = strip_version(name)
        name = name if name in packages else providers.get(name, name)
        if name in selected:
            return
        if name not in packages:
            raise ValueError(f"Unresolved MSYS2 dependency: {name}")
        selected.add(name)
        for dependency in packages[name].get("DEPENDS", []):
            visit(dependency)

    visit(ROOT_PACKAGE)
    return [packages[name] for name in sorted(selected)]


def download_package(fields, cache):
    filename = fields["FILENAME"][0]
    if Path(filename).name != filename:
        raise ValueError("Invalid package filename")
    path = cache / filename
    expected = fields["SHA256SUM"][0]
    if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == expected:
        return path
    data = get_bytes(BASE + filename)
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f"SHA256 mismatch: {filename}")
    path.write_bytes(data)
    print("Verified:", fields["NAME"][0], flush=True)
    return path


def extract_runtime(package, runtime):
    count = 0
    with package.open("rb") as stream:
        with zstandard.ZstdDecompressor().stream_reader(stream) as reader:
            with tarfile.open(fileobj=reader, mode="r|") as archive:
                for member in archive:
                    name = PurePosixPath(member.name)
                    is_dll = name.parts[:2] == ("ucrt64", "bin") and name.suffix.lower() == ".dll"
                    is_data = any(member.name.startswith(prefix) for prefix in (
                        "ucrt64/share/libthai/", "ucrt64/share/licenses/",
                    ))
                    if not member.isfile() or not (is_dll or is_data):
                        continue
                    target = runtime.joinpath(*name.parts).resolve()
                    if not target.is_relative_to(runtime) or name.is_absolute() or ".." in name.parts:
                        raise ValueError(f"Unsafe package member: {member.name}")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(archive.extractfile(member).read())
                    count += int(is_dll)
    return count


def configure_startup(runtime, prefix):
    fonts = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    cache = runtime / "font-cache"
    cache.mkdir(exist_ok=True)
    (runtime / "fonts.conf").write_text(
        '<?xml version="1.0"?>\n<fontconfig>\n'
        f'  <dir>{escape(fonts.as_posix())}</dir>\n'
        f'  <cachedir>{escape(cache.as_posix())}</cachedir>\n'
        '  <alias><family>serif</family><prefer><family>Times New Roman</family>'
        '<family>SimSun</family></prefer></alias>\n'
        '  <alias><family>sans-serif</family><prefer><family>Segoe UI</family>'
        '<family>Microsoft YaHei</family></prefer></alias>\n'
        '</fontconfig>\n', encoding="utf-8",
    )
    site = prefix / "Lib" / "site-packages"
    bootstrap = site / "_project2_weasyprint_runtime.py"
    pth = site / "weasyprint_runtime.pth"
    marker = "# Project2 WeasyPrint native runtime"
    for path in (bootstrap, pth):
        if path.exists() and marker not in path.read_text(encoding="utf-8"):
            raise FileExistsError(f"Refusing to overwrite unrelated startup file: {path}")
    bootstrap.write_text(
        marker + '\nimport os\nimport sys\nfrom pathlib import Path\n\n'
        'if os.name == "nt":\n'
        '    runtime = Path(sys.prefix) / "weasyprint-runtime"\n'
        '    dlls = runtime / "ucrt64" / "bin"\n'
        '    if dlls.is_dir():\n'
        '        existing = os.environ.get("WEASYPRINT_DLL_DIRECTORIES", "")\n'
        '        paths = [str(dlls)] + [p for p in existing.split(";") if p and p != str(dlls)]\n'
        '        os.environ["WEASYPRINT_DLL_DIRECTORIES"] = ";".join(paths)\n'
        '        os.environ.setdefault("FONTCONFIG_FILE", str(runtime / "fonts.conf"))\n',
        encoding="utf-8",
    )
    pth.write_text(marker + "\nimport _project2_weasyprint_runtime\n", encoding="utf-8")


def main():
    expected = (Path(__file__).resolve().parents[1] / ".venv").resolve()
    prefix = Path(sys.prefix).resolve()
    if os.name != "nt" or prefix != expected or sys.maxsize <= 2**32:
        raise SystemExit("Run using this project's 64-bit .venv\\Scripts\\python.exe on Windows")
    runtime = (prefix / "weasyprint-runtime").resolve()
    runtime.mkdir(exist_ok=True)
    cache = runtime / "packages"
    cache.mkdir(exist_ok=True)
    packages = dependency_closure(read_database())
    print("Official MSYS2 packages:", len(packages), flush=True)
    print("Download MiB:", round(sum(int(p["CSIZE"][0]) for p in packages) / 2**20, 1), flush=True)
    downloaded = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(download_package, fields, cache): fields for fields in packages}
        for future in as_completed(futures):
            fields = futures[future]
            downloaded[fields["NAME"][0]] = future.result()
    dll_count = sum(extract_runtime(downloaded[p["NAME"][0]], runtime) for p in packages)
    configure_startup(runtime, prefix)
    manifest = [{
        "name": p["NAME"][0], "version": p["VERSION"][0],
        "url": BASE + p["FILENAME"][0], "sha256": p["SHA256SUM"][0],
    } for p in packages]
    (runtime / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Runtime DLLs extracted:", dll_count)
    print("Runtime directory:", runtime)
    print("Restart the Python process to activate its virtualenv startup configuration.")


if __name__ == "__main__":
    main()
