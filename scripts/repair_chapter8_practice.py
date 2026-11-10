"""Apply the reviewed, chapter-eight-only repairs to the saved exercise.

Dry-run by default. --apply requires an exact original hash and saves a backup.
Never imports or executes the exercise, its project imports, or environment files.
"""

import argparse
import ast
import datetime
import difflib
import hashlib
from pathlib import Path


PRACTICE = Path(r"D:\桌面\新建文件夹\1.py")

HTTP_ADAPTER = '''async def write_report(request: ResearchRequest):
    if request.report_type == "multi_agents":
        team_model = app.state.team_model
        if team_model is None:
            raise HTTPException(
                status_code=503,
                detail="多 Agent 模型调用函数尚未装配",
            )

        state = await run_multi_agent_task(
            query=request.task,
            call_model=team_model,
            source=request.report_source,
        )
        report = state["report"]
        report_source = request.report_source
        researcher_information = {
            "source_urls": None,
            "research_costs": None,
            "references": state["sources"],
        }
    else:
        report, researcher = await run_agent(
            request.task,
            request.report_source,
            request.report_type,
            return_researcher=True,
        )
        report_source = researcher.report_source
        researcher_information = {
            "source_urls": researcher.get_source_urls(),
            "research_costs": researcher.get_costs(),
        }

    docx_path = await write_md_to_word(report, "practice_report")
    pdf_path = await write_md_to_pdf(report, "practice_report")
    return {
        "task": request.task,
        "report_source": report_source,
        "report": report,
        "researcher_information": researcher_information,
        "docx_path": docx_path,
        "pdf_path": pdf_path,
    }'''


def patched(source):
    def replace(old, new, count=1):
        nonlocal source
        actual = source.count(old)
        if actual != count:
            raise RuntimeError(f"Refusing changed input: expected {count}, found {actual}: {old!r}")
        source = source.replace(old, new)

    if "app.state.team_model = None" not in source:
        replace("app = FastAPI()\n", "app = FastAPI()\napp.state.team_model = None\n")
    replace("async def run_depth_research(self,state:ResearchState):", "async def run_depth_research(self,state:DraftState):")
    replace("self.reviser=ReviewerAgent(call_model)", "self.reviser=ReviserAgent(call_model)")
    replace("task=state[task]", 'task=state["task"]', 2)
    replace("init_research=state[init_research]", 'init_research=state["initial_research"]')
    replace('max_sections = task.get("max_sections", 3)\n', 'max_sections = task.get("max_sections", 3)\n        if max_sections < 1:\n            raise ValueError("章节数量上限必须大于零")\n')
    replace('plan = json.loads(response)\n        title =', 'plan = json.loads(response)\n        if not isinstance(plan, dict):\n            raise ValueError("章节规划必须是 JSON 对象")\n        title =')
    replace('    async def run_parallel_research(self, state: ResearchState):', '        return workflow\n\n    async def run_parallel_research(self, state: ResearchState):')
    replace('        draft=state["draft"]\n', '        draft=state["draft"][topic]\n')
    replace('        revision=json.loads(response)\n', '        revision=json.loads(response)\n        if not isinstance(revision, dict) or not isinstance(revision.get("draft"), dict):\n            raise ValueError("修改结果必须包含 draft 字典")\n')
    replace('"planer"', '"planner"', 3)
    replace('"accept":"research",', '"accept":"researcher",')
    replace('        workflow.add_edge("researcher", "writer")\n        workflow.add_edge("researcher", "writer")', '        workflow.add_edge("researcher", "writer")')
    replace('result= await chain.invoke(', 'result= await chain.ainvoke(')

    tree = ast.parse(source)
    old = next(n for n in tree.body if isinstance(n, ast.AsyncFunctionDef) and n.name == "write_report")
    if "run_multi_agent_task(" not in ast.get_source_segment(source, old):
        lines = source.splitlines(keepends=True)
        lines[old.lineno - 1:old.end_lineno] = [HTTP_ADAPTER + "\n"]
        source = "".join(lines)
    compile(source, str(PRACTICE), "exec")
    return source


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--expected-sha256")
    args = parser.parse_args()
    raw = PRACTICE.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    original = raw.decode("utf-8-sig").replace("\r\n", "\n")
    candidate = patched(original)
    print("Original SHA256:", digest)
    if not args.apply:
        print("".join(difflib.unified_diff(original.splitlines(True), candidate.splitlines(True), fromfile="saved", tofile="reviewed")))
        print("Dry run: candidate compiles; no practice file or backup written.")
        return
    if not args.expected_sha256 or digest != args.expected_sha256.lower():
        raise RuntimeError("Original hash changed or missing; refusing to overwrite")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = PRACTICE.with_name(PRACTICE.name + ".before-chapter8-" + stamp + ".bak")
    if backup.exists() or PRACTICE.read_bytes() != raw:
        raise RuntimeError("Backup exists or exercise changed; refusing to overwrite")
    backup.write_bytes(raw)
    newline = "\r\n" if b"\r\n" in raw else "\n"
    result = candidate.replace("\n", newline).encode("utf-8")
    if raw.startswith(b"\xef\xbb\xbf"):
        result = b"\xef\xbb\xbf" + result
    PRACTICE.write_bytes(result)
    print("Backup:", backup)
    print("Updated SHA256:", hashlib.sha256(result).hexdigest())


if __name__ == "__main__":
    main()
