"""Check saved chapter 10 helpers with real local MCP and fixed model replies.

AST loading avoids practice imports, dotenv and HTTP startup. No provider request
or credential is needed. MCP discovery and execution use the actual SDK/process.
"""

import ast
import asyncio
import hashlib
import json
import os
from pathlib import Path

os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool


PRACTICE = Path(r"D:\桌面\新建文件夹\1.py")
PASSED = []


def passed(name):
    PASSED.append(name)
    print(f"PASS {len(PASSED):02d}: {name}", flush=True)


def load_helpers():
    raw = PRACTICE.read_bytes()
    tree = ast.parse(raw.decode("utf-8-sig"), filename=str(PRACTICE))
    names = {"make_model_caller", "run_tool_agent", "load_mcp_tools", "run_knowledge_agent",
             "mcp_results_to_materials"}
    nodes = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
             and n.name in names]
    assert {n.name for n in nodes} == names, "Some helper functions have not been saved"
    ns = {"json": json}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(PRACTICE), "exec"), ns)
    return raw, ns


class FixedModel:
    def __init__(self, replies):
        self.replies = list(replies)
        self.histories = []
        self.names = []

    def bind_tools(self, tools):
        self.names = [t.name for t in tools]
        return self

    async def ainvoke(self, messages):
        self.histories.append(list(messages))
        assert self.replies, "Unexpected extra model invocation"
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        if callable(reply):
            return reply(messages)
        return reply


def request(name, args, call_id="call_1"):
    return AIMessage(content="", tool_calls=[{
        "name": name, "args": args, "id": call_id, "type": "tool_call",
    }])


async def expect_error(exc_type, coro):
    try:
        await coro
    except exc_type:
        return
    raise AssertionError(f"Expected {exc_type.__name__}")


async def main():
    raw, ns = load_helpers()
    run = ns["run_tool_agent"]
    load = ns["load_mcp_tools"]
    entry = ns["run_knowledge_agent"]
    passed("saved practice file parses; helpers extracted without running imports")

    caller = ns["make_model_caller"](FixedModel([AIMessage(content="  正文  ")]))
    assert await caller([]) == "正文"
    empty = ns["make_model_caller"](FixedModel([AIMessage(content="  ")]))
    await expect_error(ValueError, empty([]))
    passed("text adapter returns stripped text and rejects empty output")

    await expect_error(ValueError, load({}))
    passed("empty MCP configuration fails explicitly")

    # Capture the saved entry's configuration while retaining the real loader.
    saved_configs = []
    async def capture(configs):
        saved_configs.append(configs)
        return await load(configs)
    ns["load_mcp_tools"] = capture

    def after_search(history):
        last = history[-1]
        assert isinstance(last, ToolMessage)
        assert last.tool_call_id == "search_1" and last.status == "success"
        assert "doc_1" in last.content
        assert "发票" not in last.content, "Search should return metadata, not body"
        return request("knowledge_read_doc", {"doc_id": "doc_1"}, "read_1")

    def after_read(history):
        last = history[-1]
        assert isinstance(last, ToolMessage)
        assert last.tool_call_id == "read_1" and last.status == "success"
        assert "发票" in last.content and "主管审批" in last.content
        return AIMessage(content="演示规定要求提供发票，并由主管审批。")

    model = FixedModel([
        request("knowledge_search_docs", {"query": "报销"}, "search_1"),
        after_search,
        after_read,
    ])
    answer, results = await asyncio.wait_for(entry(model, "报销需要什么材料？"), 45)
    assert set(model.names) == {"knowledge_search_docs", "knowledge_read_doc"}
    passed("real MCP stdio discovers both tools with server name prefixes")
    assert len(model.histories) == 3 and len(results) == 2
    assert all(r["status"] == "success" for r in results)
    assert "发票" in answer
    passed("saved entry completes search -> read -> answer with matching ToolMessage IDs")

    materials = ns["mcp_results_to_materials"](results)
    assert len(materials) == 1
    assert materials[0]["url"] == "mcp://knowledge/doc_1"
    assert materials[0]["title"] == "报销规定"
    assert "发票" in materials[0]["raw_content"]
    assert results[1]["args"] == {"doc_id": "doc_1"}
    passed("real MCP body becomes a research material with its requested document ID")

    invalid = [
        {"tool": "knowledge_read_doc", "status": "error", "result": "failed"},
        {"tool": "knowledge_search_docs", "status": "success", "result": []},
        {"tool": "knowledge_read_doc", "status": "success", "args": {"doc_id": "d"},
         "result": [{"type": "text", "text": "not JSON"}]},
        {"tool": "knowledge_read_doc", "status": "success", "args": {"doc_id": "d"},
         "result": [{"type": "text", "text": json.dumps({"content": "  "})}]},
        {"tool": "knowledge_read_doc", "status": "success", "args": {},
         "result": [{"type": "text", "text": json.dumps({"content": "正文"})}]},
    ]
    assert ns["mcp_results_to_materials"](invalid) == []
    passed("errors, search metadata, invalid JSON, blank bodies and missing IDs are excluded")

    tools = await asyncio.wait_for(load(saved_configs[0]), 20)
    by_name = {t.name: t for t in tools}
    missing = await by_name["knowledge_search_docs"].ainvoke({"query": "不存在的主题"})
    assert "doc_1" not in str(missing)
    passed("real MCP search with no match returns no document")

    def after_error(history):
        last = history[-1]
        assert isinstance(last, ToolMessage) and last.status == "error"
        assert last.tool_call_id == "bad_doc"
        return AIMessage(content="文档读取失败，无法根据正文回答。")

    error_model = FixedModel([
        request("knowledge_read_doc", {"doc_id": "missing"}, "bad_doc"), after_error,
    ])
    _, failures = await run(error_model, [], tools)
    assert failures[0]["status"] == "error"
    passed("real MCP tool error becomes an error ToolMessage for the model")

    unknown = FixedModel([
        request("unknown_tool", {}, "bad_doc"), after_error,
    ])
    _, failures = await run(unknown, [], tools)
    assert failures[0]["status"] == "error"
    passed("unknown tool name becomes an error message rather than aborting the loop")

    executed = []
    @tool
    async def probe() -> str:
        """Record whether a tool was executed."""
        executed.append(True)
        return "ok"

    capped = FixedModel([request("probe", {})])
    await expect_error(RuntimeError, run(capped, [], [probe], max_rounds=1))
    assert not executed
    passed("round limit stops before executing a final unanswerable tool batch")

    duplicate = FixedModel([])
    await expect_error(ValueError, run(duplicate, [], [probe, probe]))
    await expect_error(ValueError, run(duplicate, [], [], max_rounds=0))
    assert not duplicate.histories
    passed("duplicate tools and invalid round limit fail before model invocation")

    messages = [{"role": "user", "content": "你好"}]
    original = list(messages)
    answer, results = await run(FixedModel([AIMessage(content="你好")]), messages, [])
    assert messages == original and answer == "你好" and results == []
    await expect_error(ValueError, run(FixedModel([AIMessage(content=" ")]), [], []))
    passed("tool-free answer works, blank answer fails, caller history is not mutated")

    await expect_error(RuntimeError, run(FixedModel([RuntimeError("fixed model failure")]), [], []))
    passed("model failures propagate explicitly")
    assert PRACTICE.read_bytes() == raw, "Checks must not modify practice code"
    print(f"\n{len(PASSED)} checks passed; SHA256={hashlib.sha256(raw).hexdigest()}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
