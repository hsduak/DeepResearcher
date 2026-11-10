# DeepResearcher

A research and report-generation application with web retrieval, local-document context, and multiple agent workflows.

## Main modules

- `gpt_researcher/`: query planning, retrieval, scraping, context selection, and report writing.
- `multi_agents/`: explicit role and workflow orchestration.
- `deep_agents/`: chief-editor / researcher delegation with file-based drafts.
- `backend/` and `frontend/`: HTTP, WebSocket, and web interfaces.
- `mcp-server/`: MCP example tools.
- `milvus-demo/`: a local Milvus deployment and functional checks.
- `evals/` and `tests/`: evaluation and test code.

## Local development

Use Python 3.11 or newer. Create a virtual environment, install `requirements.txt`, and provide the provider credentials required by your chosen configuration in a local `.env` file. Do not commit credentials.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

For the Next.js interface, install dependencies in `frontend/nextjs` and run `npm run dev`.

The workflows are alternative execution paths; they are not one combined sequential pipeline. External model, search, and database services require separate configuration. The Milvus demo README documents its local setup. Some study validation scripts refer to an external handwritten practice file and require that file to run.

## License and notices

See `LICENSE` and `NOTICE` for the applicable license, retained third-party attribution, and distribution modifications.
