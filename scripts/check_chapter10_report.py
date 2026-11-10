"""Check saved MCP -> research state -> report orchestration and HTTP injection.

One complete report uses the real local stdio MCP server. Model replies and
embeddings are fixed; no credentials, dotenv, public APIs or real exports run.
Additional failure/HTTP cases isolate MCP data with fixed tool-result fixtures.
"""

import asyncio
import hashlib
import json
import os

os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

import httpx
from langchain_core.messages import AIMessage, ToolMessage

from check_chapter6 import Fixture, PRACTICE, expect_error, load_practice
from check_chapter10_mcp import FixedModel, request


PASSED = []
ROLE = AIMessage(content=json.dumps({
    "server": "知识库研究员", "agent_role_prompt": "根据取得的文档正文撰写报告。",
}, ensure_ascii=False))
BODY = "演示规定：报销需要提供发票，并由主管审批。"


def passed(name):
    PASSED.append(name)
    print(f"PASS {len(PASSED):02d}: {name}", flush=True)


async def forbidden_search(query):
    raise AssertionError("A pure MCP report must not call the web search fixture")


async def fixed_materials(**kwargs):
    return "助手草稿不能当作原始正文", [{
        "tool": "knowledge_read_doc", "args": {"doc_id": "doc_1"},
        "status": "success", "result": [{
            "type": "text", "text": json.dumps({
                "title": "报销规定", "content": BODY,
            }, ensure_ascii=False),
        }],
    }]


def final_report(messages):
    prompt = messages[-1]["content"]
    assert BODY in prompt and "mcp://knowledge/doc_1" in prompt
    assert "助手草稿" not in prompt
    return AIMessage(content="# MCP 演示报告\n\n根据演示文档，需提供发票并由主管审批。")


async def main():
    raw, ns = load_practice()
    fixture = Fixture(ns)
    ns["search_web"] = forbidden_search

    def read_request(history):
        last = history[-1]
        assert isinstance(last, ToolMessage) and last.status == "success"
        assert "doc_1" in last.content
        return request("knowledge_read_doc", {"doc_id": "doc_1"}, "read_1")

    def interim_answer(history):
        last = history[-1]
        assert isinstance(last, ToolMessage) and BODY in last.content
        return AIMessage(content="助手草稿：演示政策摘要。")

    model = FixedModel([
        ROLE,
        request("knowledge_search_docs", {"query": "报销"}, "search_1"),
        read_request,
        interim_answer,
        final_report,
    ])
    report, owner = await asyncio.wait_for(ns["run_agent"](
        "报销需要什么材料？", "mcp", "research_report",
        return_researcher=True, chat_model=model,
    ), 60)
    assert len(model.histories) == 5 and not model.replies
    assert len(owner.research_sources) == 1 and owner.research_sources[0]["raw_content"] == BODY
    passed("saved report entry runs real MCP search/read and stores original document body")

    assert isinstance(owner.context, list) and len(owner.context) == 1
    assert BODY in owner.context[0] and "Source: mcp://knowledge/doc_1" in owner.context[0]
    assert not fixture.scraped and not owner.visited_urls
    passed("existing ContextManager formats MCP evidence without scraping a synthetic URL")

    assert report.count("## 资料来源") == 1
    assert report.count("mcp://knowledge/doc_1") == 1
    assert "助手草稿" not in report and "发票" in report
    passed("report writing uses document context and appends the internal source identifier")

    # These cases use fixed MCP outputs to isolate the controller's boundaries.
    calls = []
    async def empty_materials(**kwargs):
        calls.append(kwargs)
        return "没有资料", []

    ns["run_knowledge_agent"] = empty_materials
    missing_model = ns["GPTResearcher"]("报销", "mcp", "research_report")
    missing_model.agent = missing_model.role = "fixture"
    await expect_error(ValueError, missing_model.conduct_research())
    assert not calls
    passed("missing client fails before attempting MCP work")

    empty_owner = ns["GPTResearcher"]("报销", "mcp", "research_report", chat_model=FixedModel([]))
    empty_owner.agent = empty_owner.role = "fixture"
    await expect_error(ValueError, empty_owner.conduct_research())
    assert calls and empty_owner.research_sources == [] and empty_owner.context == []
    passed("no document body fails research instead of generating an unsupported report")

    ns["run_knowledge_agent"] = fixed_materials
    empty_context_owner = ns["GPTResearcher"]("报销", "mcp", "research_report", chat_model=FixedModel([]))
    empty_context_owner.agent = empty_context_owner.role = "fixture"
    async def empty_context(query, materials):
        return ""
    empty_context_owner.context_manager.get_similar_content_by_query = empty_context
    await expect_error(ValueError, empty_context_owner.conduct_research())
    assert len(empty_context_owner.research_sources) == 1 and empty_context_owner.context == []
    passed("empty processed context fails explicitly while retaining collected source state")

    http_model = FixedModel([ROLE, final_report])
    ns["app"].state.chat_model = http_model
    transport = httpx.ASGITransport(app=ns["app"])
    async with httpx.AsyncClient(transport=transport, base_url="http://exercise") as client:
        response = await client.post("/report/", json={
            "task": "报销需要什么材料？", "report_source": "mcp",
            "report_type": "research_report",
        })
        assert response.status_code == 200, response.text
        result = response.json()
        assert fixture.researchers[-1].chat_model is http_model
        assert len(http_model.histories) == 2 and result["report_source"] == "mcp"
        assert result["researcher_information"]["source_urls"] == ["mcp://knowledge/doc_1"]
        assert result["docx_path"] == "outputs/fixture.docx"
        assert result["pdf_path"] == "outputs/fixture.pdf"
        assert len(fixture.exports) == 2
        invalid = await client.post("/report/", json={"report_source": "mcp"})
        assert invalid.status_code == 422
    passed("HTTP entry passes application client; response/source fields and export interfaces remain valid")

    assert PRACTICE.read_bytes() == raw
    print(f"\n{len(PASSED)} checks passed; SHA256={hashlib.sha256(raw).hexdigest()}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
