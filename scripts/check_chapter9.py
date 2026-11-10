"""Offline checks of saved tools, real Deep Agents runtime and file output.

AST loading skips practice imports, dotenv and server startup. Existing saved
research/document/writing orchestration runs with external search, scraping,
embedding and writing doubles. The outer ChatModel is also a fixed double;
Deep Agents, its task/file tools and FilesystemBackend are real.
"""

import asyncio
import hashlib
import json
import os
import socket
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from pydantic import Field

from check_chapter6 import Fixture, load_practice, expect_error


ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "outputs" / "chapter9_checks"
PASSED = []


def passed(name):
    PASSED.append(name)
    print(f"PASS {len(PASSED):02d}: {name}", flush=True)


class ScriptedResearchModel(BaseChatModel):
    """Fixed tool decisions; never uses a provider, token or network service."""

    scenario: str = "normal"
    events: list = Field(default_factory=list)
    bindings: list = Field(default_factory=list)
    chapter_content: str = ""

    @property
    def _llm_type(self):
        return "chapter9-offline-script"

    def bind_tools(self, tools, **kwargs):
        names = [t.get("name") if isinstance(t, dict) else t.name for t in tools]
        self.bindings.append(set(names))
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        system = "\n".join(str(m.content) for m in messages if isinstance(m, SystemMessage))
        child = "你负责研究报告中的一个章节" in system
        role = "researcher" if child else "chief"
        last = messages[-1]
        self.events.append((role, getattr(last, "name", None), str(last.content)))

        def call(name, args):
            return AIMessage(content="", tool_calls=[{
                "name": name, "args": args, "id": f"c{len(self.events)}", "type": "tool_call",
            }])

        if self.scenario == "missing":
            response = AIMessage(content="仅回复摘要，没有保存文件。")
        elif self.scenario == "empty":
            if isinstance(last, ToolMessage):
                response = AIMessage(content="已保存空文件。")
            else:
                response = call("write_file", {"file_path": "/report.md", "content": "  \n"})
        elif self.scenario == "error":
            raise RuntimeError("fixed model failure")
        elif child:
            if isinstance(last, ToolMessage) and last.name == "deep_research":
                assert last.status != "error", last.content
                self.chapter_content = str(last.content)
                assert "### Sources" in self.chapter_content
                response = call("write_file", {
                    "file_path": "/sections/01-retrieval.md", "content": self.chapter_content,
                })
            elif isinstance(last, ToolMessage) and last.name == "write_file":
                assert last.status != "error", last.content
                response = AIMessage(content="章节已完成，草稿：/sections/01-retrieval.md")
            else:
                humans = [m for m in messages if isinstance(m, HumanMessage)]
                assert len(humans) == 1, "Child receives only delegated description"
                payload = json.loads(str(humans[0].content))
                assert payload["path"] == "/sections/01-retrieval.md"
                assert not any(isinstance(m, ToolMessage) for m in messages)
                response = call("deep_research", {
                    "query": payload["query"], "parent_query": payload["parent_query"],
                })
        elif isinstance(last, ToolMessage):
            assert last.status != "error", last.content
            if last.name == "quick_search":
                response = call("task", {
                    "subagent_type": "researcher",
                    "description": json.dumps({
                        "query": "RAG 检索遗漏", "parent_query": "RAG 如何减少幻觉",
                        "path": "/sections/01-retrieval.md",
                    }, ensure_ascii=False),
                })
            elif last.name == "task":
                assert "草稿" in str(last.content)
                assert "### Sources" not in str(last.content), "Parent initially gets short child reply"
                response = call("read_file", {"file_path": "/sections/01-retrieval.md"})
            elif last.name == "read_file":
                assert "### Sources" in str(last.content)
                body, sources = self.chapter_content.split("\n\n### Sources\n\n", 1)
                report = "# RAG 如何减少幻觉\n\n## 引言\n\n研究检索证据。\n\n" + body
                report += "\n\n## 结论\n\n需要核对证据。\n\n## References\n\n" + sources
                response = call("write_file", {"file_path": "/report.md", "content": report})
            elif last.name == "write_file":
                response = AIMessage(content="报告已完成，见 /report.md。")
            else:
                raise AssertionError(f"Unexpected chief tool: {last.name}")
        else:
            response = call("quick_search", {"query": "RAG 如何减少幻觉"})

        return ChatResult(generations=[ChatGeneration(message=response)])


async def check_tools():
    _, ns = load_practice()
    fixture = Fixture(ns)
    created = len(fixture.researchers)
    tools = ns["build_research_tools"]({"source": "web"})
    assert set(tools) == {"quick_search", "deep_research"}
    assert len(fixture.researchers) == created
    passed("Factory creates callable tools without starting research")

    async def search(query):
        return [
            {"title": "A", "body": "摘要甲", "href": "https://a.invalid/a"},
            {"title": "B", "content": "摘要乙", "url": "https://b.invalid/b"},
        ]

    ns["search_web"] = search
    text = await tools["quick_search"]("RAG")
    assert text == "[1] A\n摘要甲\nURL: https://a.invalid/a\n\n[2] B\n摘要乙\nURL: https://b.invalid/b"
    assert len(fixture.researchers) == created
    passed("Quick search formats both result field styles without full research")

    async def empty_search(query):
        return []

    ns["search_web"] = empty_search
    assert await tools["quick_search"]("RAG") == "没有找到搜索结果。"
    passed("Empty quick search returns an explicit message")

    async def failed_search(query):
        raise RuntimeError("fixed search failure")

    ns["search_web"] = failed_search
    await expect_error(RuntimeError, tools["quick_search"]("RAG"))
    passed("Quick-search exceptions propagate")

    ns["search_web"] = fixture.search
    section = await tools["deep_research"]("RAG 检索遗漏", "RAG 如何减少幻觉")
    r = fixture.researchers[-1]
    assert r.report_type == "subtopic_report" and r.report_source == "web"
    assert r.context and r.research_sources
    assert "整篇报告的总问题：RAG 如何减少幻觉" in fixture.writes[-1][1]
    assert section.count("### Sources") == 1
    assert all(url in section for url in r.get_source_urls())
    passed("Saved full research pipeline carries parent topic and chapter sources")

    full = await tools["deep_research"]("RAG")
    assert fixture.researchers[-1].report_type == "research_report"
    assert "## 资料来源" in full and "### Sources" not in full
    assert fixture.researchers[-1] is not r
    passed("Full report retains existing references and per-call isolated state")

    class StubResearcher:
        instances = []

        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.__class__.instances.append(self)

        async def conduct_research(self):
            return []

        async def write_report(self, **kwargs):
            return "## empty-source chapter"

        def get_source_urls(self):
            return []

    ns["GPTResearcher"] = StubResearcher
    task = {"source": "hybrid"}
    tools = ns["build_research_tools"](task)
    task["source"] = "local"
    report = await tools["deep_research"]("chapter", "parent")
    assert StubResearcher.instances[-1].kwargs["report_source"] == "hybrid"
    assert "Sources" not in report
    passed("Source is captured at factory creation; empty sources add no heading")

    class FailedResearcher(StubResearcher):
        async def conduct_research(self):
            raise RuntimeError("fixed research failure")

        async def write_report(self, **kwargs):
            raise AssertionError("Writing must not follow research failure")

    ns["GPTResearcher"] = FailedResearcher
    await expect_error(RuntimeError, tools["deep_research"]("chapter", "parent"))
    passed("Research failure stops before writing")


async def check_runtime(base):
    _, ns = load_practice()
    fixture = Fixture(ns)
    run = ns["run_deep_agent_task"]
    model = ScriptedResearchModel()
    result = await asyncio.wait_for(run(
        "RAG 如何减少幻觉", model, str(base / "normal"),
    ), timeout=60)
    report = Path(result["report_path"])
    assert report.is_absolute() and report.is_file()
    assert report.read_text(encoding="utf-8") == result["report"]
    assert result["report"].startswith("# RAG 如何减少幻觉")
    assert result["report"] != "报告已完成，见 /report.md。"
    passed("Real SDK executes task delegation, reads draft and writes UTF-8 final report")

    chapter = report.parent / "sections" / "01-retrieval.md"
    assert chapter.read_text(encoding="utf-8") == model.chapter_content
    assert "### Sources" in model.chapter_content
    assert "## References" in result["report"] and "### Sources" not in result["report"]
    assert len(fixture.researchers) == 1
    assert any("task" in names and "deep_research" not in names for names in model.bindings)
    assert any("deep_research" in names for names in model.bindings)
    assert sum(role == "chief" and name == "task" for role, name, _ in model.events) == 1
    passed("Child context, function tools, shared output files and reference transfer work")

    calls = len(model.events)
    await expect_error(FileExistsError, run("RAG", model, str(report.parent)))
    assert len(model.events) == calls
    passed("Existing report is rejected before model execution")

    await expect_error(FileNotFoundError, run(
        "RAG", ScriptedResearchModel(scenario="missing"), str(base / "missing"),
    ))
    passed("Successful chat without report.md raises FileNotFoundError")

    await expect_error(ValueError, run(
        "RAG", ScriptedResearchModel(scenario="empty"), str(base / "empty"),
    ))
    passed("Real SDK can write a blank file; entry rejects empty report")

    await expect_error(RuntimeError, run(
        "RAG", ScriptedResearchModel(scenario="error"), str(base / "error"),
    ))
    passed("Model failure propagates without fake success")


async def main():
    raw, _ = load_practice()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix="run-", dir=SCRATCH) as tmp:
        base = Path(tmp).resolve()
        assert base.parent == SCRATCH.resolve()
        with patch.object(socket, "create_connection", side_effect=AssertionError("Network forbidden")), \
             patch.object(socket.socket, "connect", side_effect=AssertionError("Network forbidden")):
            await check_tools()
            await check_runtime(base)
    print(f"\n{len(PASSED)} checks passed; SHA256={hashlib.sha256(raw).hexdigest()}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
