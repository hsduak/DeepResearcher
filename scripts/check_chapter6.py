"""Check saved chapter-six practice code without keys, network or database calls.

AST loading skips imports and the server startup block. Saved orchestration,
document conversion, splitting, EmbeddingsFilter, writing and HTTP handlers run;
search, page fetching, Embeddings, model calls and export outputs are doubles.
"""

import ast
import asyncio
import hashlib
import json
from pathlib import Path
from typing import TypedDict
from urllib.parse import quote

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from langchain_classic.retrievers.document_compressors import EmbeddingsFilter
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import StateGraph, END
from pydantic import BaseModel


PRACTICE = Path(r"D:\桌面\新建文件夹\1.py")
PASSED = []


def passed(name):
    PASSED.append(name)
    print(f"PASS {len(PASSED):02d}: {name}", flush=True)


class FixtureEmbeddings(Embeddings):
    """Deterministic vectors exercise filtering, not semantic quality."""

    def __init__(self):
        self.calls = 0

    def embed_documents(self, texts):
        self.calls += 1
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text):
        assert isinstance(text, str), "Embedding input must be document text"
        return [1.0, 0.1 * ("原理" in text), 0.1 * ("局限" in text), 0.1]


def load_practice():
    raw = PRACTICE.read_bytes()
    source = raw.decode("utf-8-sig")
    compile(source, str(PRACTICE), "exec")
    nodes = [node for node in ast.parse(source).body
             if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))]
    namespace = {
        "asyncio": asyncio, "json": json, "Path": Path,
        "app": FastAPI(), "HTTPException": HTTPException, "BaseModel": BaseModel,
        "Document": Document, "RecursiveCharacterTextSplitter": RecursiveCharacterTextSplitter,
        "EmbeddingsFilter": EmbeddingsFilter,
        "OpenAIEmbeddings": lambda **kwargs: FixtureEmbeddings(),
        "TypedDict": TypedDict, "StateGraph": StateGraph, "END": END,
    }
    namespace["app"].state.team_model = None
    namespace["app"].state.chat_model = None
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(PRACTICE), "exec"), namespace)
    return raw, namespace


class Fixture:
    def __init__(self, namespace):
        self.ns = namespace
        self.researchers = []
        self.detailed = []
        self.scraped = []
        self.writes = []
        self.exports = []
        researcher_class = namespace["GPTResearcher"]
        detailed_class = namespace["DetailedReport"]

        def researcher(*args, **kwargs):
            result = researcher_class(*args, **kwargs)
            self.researchers.append(result)
            return result

        def detailed(*args, **kwargs):
            result = detailed_class(*args, **kwargs)
            self.detailed.append(result)
            return result

        namespace.update({
            "GPTResearcher": researcher, "DetailedReport": detailed,
            "search_web": self.search, "scrape_page": self.scrape,
            "demo_write_model": self.write,
            "write_md_to_word": self.word, "write_md_to_pdf": self.pdf,
        })

    async def search(self, query):
        return [
            {"url": "https://fixture.invalid/shared"},
            {"url": "https://fixture.invalid/" + quote(query, safe="")},
        ]

    def scrape(self, url):
        self.scraped.append(url)
        return {
            "url": url, "title": "测试资料",
            "raw_content": "RAG 原理涉及检索和生成，局限涉及检索遗漏和证据质量。" * 5,
        }

    async def write(self, messages):
        user = messages[-1]["content"]
        if "请撰写报告的引言" in user:
            kind, result = "引言", "## 引言\n\n讨论 RAG 的原理与局限。"
        elif "请撰写报告的结论" in user:
            assert "## RAG 的工作原理" in user
            assert "## RAG 的局限与改进" in user
            kind, result = "结论", "## 结论\n\n应关注检索与证据质量。"
        elif "本次只撰写当前章节正文" in user:
            title = user.splitlines()[0].removeprefix("研究问题")
            kind = title
            result = f"## {title}\n\nRAG 原理和局限需要证据支持。"
        else:
            kind, result = "普通报告", "# RAG 报告\n\nRAG 使用检索证据辅助生成。"
        self.writes.append((kind, user, result))
        await asyncio.sleep(0)
        return result

    async def word(self, report, filename):
        assert isinstance(report, str) and report.strip()
        self.exports.append(("word", report, filename))
        return "outputs/fixture.docx"

    async def pdf(self, report, filename):
        assert isinstance(report, str) and report.strip()
        self.exports.append(("pdf", report, filename))
        return "outputs/fixture.pdf"


async def expect_error(error_type, awaitable):
    try:
        await awaitable
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}")


async def check_core(ns, fixture):
    researcher = ns["GPTResearcher"]("RAG", "web", "research_report")
    writer = researcher.researcher_generator
    researcher.context = []
    before = len(fixture.writes)
    await expect_error(ValueError, writer.write_report())
    await expect_error(ValueError, writer.write_summary("引言", "  "))
    assert len(fixture.writes) == before
    passed("Empty research/summary content stops before model calls")

    researcher.context = ["Source: fixture\nContent: RAG 原理"]
    researcher.research_sources = [
        {"url": "https://fixture.invalid/z"}, {"url": "local.pdf"},
        {"url": "https://fixture.invalid/z"}, {"url": ""},
    ]
    researcher.visited_urls.add("https://fixture.invalid/failed")
    report = await writer.write_report()
    assert report.count("## 资料来源") == 1
    assert report.count("- [https://fixture.invalid/z]") == 1
    assert "- local.pdf" in report and "failed" not in report
    passed("Collected sources deduplicate and exclude visited-only URLs")

    original_model = researcher.write_model
    calls = []

    async def retry_model(messages):
        calls.append(messages)
        if len(calls) == 1:
            raise RuntimeError("fixture: first attempt fails")
        return "恢复后的正文"

    researcher.write_model = retry_model
    recovered = await writer.write_report()
    assert recovered.startswith("恢复后的正文") and len(calls) == 2
    assert len(calls[0]) == 2 and len(calls[1]) == 1
    assert calls[1][0]["role"] == "user"
    passed("Writing retry changes two messages into one user message")

    async def failed_model(messages):
        calls.append(messages)
        raise RuntimeError("fixture: both attempts fail")

    calls.clear()
    researcher.write_model = failed_model
    await expect_error(RuntimeError, writer.write_report())
    assert len(calls) == 2
    passed("Two model failures propagate instead of returning a coroutine")

    for invalid in (None, 123, " \n "):
        calls.clear()

        async def invalid_model(messages, value=invalid):
            calls.append(messages)
            return value

        researcher.write_model = invalid_model
        expected = ValueError if isinstance(invalid, str) else TypeError
        await expect_error(expected, writer.write_report())
        await expect_error(expected, writer.write_summary("引言", "RAG"))
        assert len(calls) == 2, "Invalid outputs fail validation without extra retry"
    researcher.write_model = original_model
    passed("Wrong-type and blank model outputs fail validation")

    child = ns["GPTResearcher"]("RAG 的局限", "web", "subtopic_report")
    child.context = ["局限的研究材料"]
    child.research_sources = [{"url": "https://fixture.invalid/chapter"}]
    chapter = await child.write_report(
        main_topic="RAG 总问题", existing_headers=["原理"],
        relevant_written_contents="前章已经介绍原理",
    )
    prompt = fixture.writes[-1][1]
    assert "RAG 总问题" in prompt and "前章已经介绍原理" in prompt
    assert "## 资料来源" not in chapter
    passed("Chapter arguments reach prompts; chapters omit final source lists")

    manager = child.context_manager
    before = manager.embeddings.calls
    assert await manager.get_similar_written_contents("RAG", []) == ""
    assert manager.embeddings.calls == before
    related = await manager.get_similar_written_contents("RAG 原理", [
        {"section_title": "原理", "written_content": "RAG 原理。" * 300},
    ])
    assert "Title: 原理" in related and manager.embeddings.calls > before
    passed("Written-content retrieval uses real Document/split/filter with fixture vectors")

    result = await ns["run_agent"]("RAG", "web", "research_report")
    assert isinstance(result, str) and "## 资料来源" in result
    result, parent = await ns["run_agent"]("RAG", "web", "research_report", True)
    assert parent.query == "RAG" and isinstance(result, str)
    passed("Ordinary routing supports both string and (report, researcher) returns")

    fixture.researchers.clear()
    fixture.writes.clear()
    fixture.scraped.clear()
    report, parent = await ns["run_agent"](
        "什么是 RAG，它有哪些局限？", "web", "detailed_report", True,
    )
    detailed = fixture.detailed[-1]
    assert parent is detailed.gpt_research
    assert len(fixture.researchers) == 3
    assert parent.report_type == "research_report"
    assert all(child.report_type == "subtopic_report" for child in fixture.researchers[1:])
    assert all(child.visited_urls is parent.visited_urls for child in fixture.researchers[1:])
    assert len(fixture.scraped) == len(set(fixture.scraped))
    assert len(parent.get_source_urls()) == len(set(fixture.scraped))
    assert report.count("## 资料来源") == 1
    positions = [report.index(part) for part in (
        "# 什么是 RAG", "## 引言", "## 目录", "## RAG 的工作原理",
        "## RAG 的局限与改进", "## 结论", "## 资料来源",
    )]
    assert positions == sorted(positions)
    assert detailed.existing_headers == ["RAG 的工作原理", "RAG 的局限与改进"]
    assert len(detailed.global_written_sections) == 2
    assert [item[0] for item in fixture.writes] == [
        "引言", "RAG 的工作原理", "RAG 的局限与改进", "结论",
    ]
    assert "相关的已写内容：\n\n" in fixture.writes[1][1]
    assert "Title: RAG 的工作原理" in fixture.writes[2][1]
    assert "1. RAG 的工作原理" in report
    passed("Detailed chain assembles in order, shares URL claims, and passes previous writing")

    previous_search = ns["search_web"]

    async def cached_search(query):
        return [{"url": "https://fixture.invalid/cached-only"}]

    ns["search_web"] = cached_search
    fixture.scraped.clear()
    cached = ns["DetailedReport"]("RAG", "web", "detailed_report")
    cached_report = await cached.run()
    assert fixture.scraped == ["https://fixture.invalid/cached-only"]
    assert len(cached.gpt_research.research_sources) == 1
    assert "## 结论" in cached_report and len(cached.global_written_sections) == 2
    ns["search_web"] = previous_search
    passed("Already-visited chapter sources reuse cached material instead of losing context")

    planner = ns["DetailedReport"]("RAG 总问题", "web", "detailed_report")
    planner.gpt_research.context = ["RAG"]

    async def malformed_plan(messages):
        return "not JSON"

    planner.subtopic_model = malformed_plan
    assert await planner._plan_subtopics() == ["RAG 总问题"]
    passed("Malformed chapter planning falls back to the original question")

    failed = ns["DetailedReport"]("RAG", "web", "detailed_report")
    failure_calls = []

    async def fail_second_chapter(messages):
        if "研究问题RAG 的局限与改进" in messages[-1]["content"]:
            failure_calls.append(messages)
            raise RuntimeError("fixture: second chapter fails")
        return await fixture.write(messages)

    failed.gpt_research.write_model = fail_second_chapter
    await expect_error(RuntimeError, failed.run())
    assert len(failure_calls) == 2
    assert failed.existing_headers == ["RAG 的工作原理"]
    assert len(failed.global_written_sections) == 1
    assert failed.gpt_research.research_sources
    passed("Chapter failure stops the report; successful history/materials remain")


def check_http(ns, fixture):
    with TestClient(ns["app"], raise_server_exceptions=False) as client:
        for report_type in ("research_report", "detailed_report"):
            response = client.post("/report/", json={"task": "RAG", "report_type": report_type})
            assert response.status_code == 200, response.text
            result = response.json()
            assert result["docx_path"] == "outputs/fixture.docx"
            assert result["pdf_path"] == "outputs/fixture.pdf"
            assert result["researcher_information"]["source_urls"]
            assert isinstance(result["report"], str)
            assert fixture.exports[-2][0] == "word" and fixture.exports[-1][0] == "pdf"
            assert fixture.exports[-2][1] == result["report"] == fixture.exports[-1][1]
        passed("HTTP ordinary/detailed responses pass identical reports to both export adapters")

        assert client.post("/report/", json={}).status_code == 422
        assert client.post("/report/", json={"task": "RAG", "report_type": "multi_agents"}).status_code == 503
        passed("HTTP missing fields give 422; unconfigured multi_agents model gives 503")

        async def empty_pdf(report, filename):
            return ""

        ns["write_md_to_pdf"] = empty_pdf
        response = client.post("/report/", json={"task": "RAG"})
        assert response.status_code == 200
        assert response.json()["pdf_path"] == "" and response.json()["report"]
        passed("An empty PDF adapter result preserves report text and Word output")

        async def failed_word(report, filename):
            raise RuntimeError("fixture: export adapter raises")

        ns["write_md_to_word"] = failed_word
        assert client.post("/report/", json={"task": "RAG"}).status_code == 500
        passed("Uncaught export errors surface as HTTP 500")


def main():
    original, namespace = load_practice()
    passed("Saved file compiles; AST load skips server startup and project imports")
    fixture = Fixture(namespace)
    asyncio.run(check_core(namespace, fixture))
    check_http(namespace, fixture)
    assert PRACTICE.read_bytes() == original, "Practice changed during verification"
    print(f"\n{len(PASSED)} checks passed. No external services or real exports called.")
    print("Practice SHA256:", hashlib.sha256(original).hexdigest())


if __name__ == "__main__":
    main()
