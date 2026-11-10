"""Check saved startup wiring without keys, provider requests or a real server."""

import ast
import asyncio
import hashlib
import os
import sys
import types
from pathlib import Path
from unittest.mock import patch


PRACTICE = Path(r"D:\桌面\新建文件夹\1.py")


def main():
    raw = PRACTICE.read_bytes()
    tree = ast.parse(raw.decode("utf-8-sig"))
    names = {"build_chat_model", "make_model_caller"}
    definitions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    entries = [n for n in tree.body if isinstance(n, ast.If) and "__name__" in ast.unparse(n.test)]
    assert len(definitions) == 2 and len(entries) == 1

    events = []
    options = {}
    messages_seen = []
    async def fake_ainvoke(messages):
        messages_seen.append(messages)
        return types.SimpleNamespace(content="启动装配测试")

    client = types.SimpleNamespace(ainvoke=fake_ainvoke)
    def fake_chat_openai(**kwargs):
        options.update(kwargs)
        events.append("client-created")
        return client

    sdk = types.ModuleType("langchain_openai")
    sdk.ChatOpenAI = fake_chat_openai
    app = types.SimpleNamespace(state=types.SimpleNamespace(chat_model=None, team_model=None))
    uvicorn = types.ModuleType("uvicorn")
    def fake_run(actual_app, **kwargs):
        assert actual_app is app and actual_app.state.chat_model is client
        assert callable(actual_app.state.team_model)
        assert kwargs["host"] == "127.0.0.1" and kwargs["port"] == 8001
        events.append("server-start")
    uvicorn.run = fake_run

    ns = {"__name__": "__main__", "app": app}
    module = ast.Module(body=definitions + entries, type_ignores=[])
    with patch.dict(sys.modules, {"langchain_openai": sdk, "uvicorn": uvicorn}), patch.dict(
        os.environ, {"DEEPSEEK_MODEL": "offline-model", "DEEPSEEK_API_KEY": "offline-placeholder"},
    ):
        exec(compile(module, str(PRACTICE), "exec"), ns)

    assert events == ["client-created", "server-start"]
    print("PASS 01: saved entry calls model factory before starting the server")
    assert options == {"model": "offline-model", "api_key": "offline-placeholder",
                       "base_url": "https://api.deepseek.com"}
    print("PASS 02: factory forwards model, credential and DeepSeek endpoint")
    assert app.state.chat_model is client and app.state.team_model is not client
    print("PASS 03: application stores raw client and a separate text adapter")
    result = asyncio.run(app.state.team_model([{"role": "user", "content": "fixture"}]))
    assert result == "启动装配测试" and len(messages_seen) == 1
    print("PASS 04: stored text adapter calls the same injected client")
    assert PRACTICE.read_bytes() == raw
    print(f"\n4 checks passed; SHA256={hashlib.sha256(raw).hexdigest()}")
    print("Provider constructor and server runner are fixtures; no real service was started.")


if __name__ == "__main__":
    main()
