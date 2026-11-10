# Windows PDF 导出环境修复

## 修复结果

项目的 `.venv\Scripts\python.exe` 已能够加载 WeasyPrint 所需的原生库。
原项目 `backend/utils.py` 的 `write_md_to_pdf` 已真实生成 PDF，中文、表格、超链接以及文件下载检查通过。

本次修复针对环境，没有替换项目原来的 PDF 转换实现。

## 原因与处理

Python 包 `weasyprint`、`md2pdf` 已安装，但 Windows 缺少 Pango/GLib 等原生 DLL。
[WeasyPrint 69 的安装说明](https://doc.courtbouillon.org/weasyprint/v69.0/first_steps.html#windows)
要求提供 Pango 及其依赖，并支持通过 `WEASYPRINT_DLL_DIRECTORIES` 指定 DLL 目录。

本项目使用 `scripts/setup_weasyprint_windows.py` 从 MSYS2 官方 UCRT64 仓库读取依赖元数据，
按索引提供的 SHA256 校验软件包，只提取运行时 DLL、辅助数据和许可证到：

```text
.venv/weasyprint-runtime/
```

- DLL：`ucrt64/bin/`。
- 字体配置：`fonts.conf`，使用系统 Windows 字体及虚拟环境内的缓存目录。
- 软件包来源、版本与校验值：`manifest.json`。
- 自动配置：`.venv/Lib/site-packages/weasyprint_runtime.pth` 和 `_project2_weasyprint_runtime.py`。

每次启动这个虚拟环境的新 Python 进程时，会设置当前进程的 DLL 搜索配置；无需在每次运行前手动设置变量。
已有 Python 进程或 API 服务需要重启。

## 重建虚拟环境后的恢复命令

在项目目录运行：

```powershell
& '.\.venv\Scripts\python.exe' '.\scripts\setup_weasyprint_windows.py'
& '.\.venv\Scripts\python.exe' -m weasyprint --info
```

安装脚本需要 `requests` 和 `zstandard`，本项目虚拟环境已提供这两个包。

## 验证记录（2026-10-26）

- WeasyPrint `69.0`，Pango `1.58.2`，Python `3.11.0` 64 位。
- 真实调用 `backend.utils.write_md_to_pdf` 成功，输出路径不再是空字符串。
- 验收 PDF 为 1 页，包含中文标题、正文、表格、列表和超链接。
- PyMuPDF 重开和文字提取通过，Poppler 渲染后目视检查通过。
- 隔离 FastAPI 静态下载验证：HTTP 200、`application/pdf`、下载字节与原文件一致。
- 验收文件：`output/pdf/pdf_environment_check.pdf`。
- 从 `D:\桌面\新建文件夹` 启动同一虚拟环境的 `weasyprint --info` 也通过。

检查中还发现练习目录的 `copy.py` 覆盖 Python 标准库 `copy`，文件本身存在未完成的缩进代码。
已将其改名为 `copy_practice.py` 并校验内容哈希不变；从该目录导入 `copy` 现已正确指向标准库。
