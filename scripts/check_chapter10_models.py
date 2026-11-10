"""Verify saved model injection through ordinary and detailed report workflows.

Research orchestration, prompts, document splitting and context filtering are
saved code. Provider responses/search/scraping/embeddings are offline fixtures.
No practice imports, dotenv, provider API or exports are executed.
"""

import asyncio
import hashlib
import os

os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

from langchain_core.messages import AIMessage
from check_chapter6 import Fixture, PRACTICE, load_practice


PASSED = []


def passed(name):
    PASSED.append(name)
    print(f"PASS {len(PASSED):02d}: {name}", flush=True)


class InjectedModel:
    """Emit valid fixed responses based on the saved prompt's requested task."""

    def __init__(self, callbacks, fixture):
        self.callbacks = callbacks
        self.fixture = fixture
        self.stages = []

    async def ainvoke(self, messages):
        system = messages[0]["content"]
        if "根据用户任务选择合适的研究角色" in system:
            stage = "role"
        elif "搜索查询" in system:
            stage = "plan"
        elif "你负责规划研究报告章节" in system:
            stage = "subtopics"
        else:
            stage = "write"
        self.stages.append(stage)
        callback = self.fixture.write if stage == "write" else self.callbacks[stage]
        return AIMessage(content=await callback(messages))


async def main():
    raw, ns = load_practice()
    callbacks = {
        "role": ns["demo_model"],
        "plan": ns["demo_plan_model"],
        "subtopics": ns["demo_subtopic_model"],
    }
    fixture = Fixture(ns)
    model = InjectedModel(callbacks, fixture)
    first = ns["GPTResearcher"]("RAG", "web", "research_report", chat_model=model)
    assert first.chat_model is model and not model.stages
    fields = ("call_model", "plan_model", "write_model", "subtopic_model",
              "deep_plan_model", "deep_query_model", "deep_extract_model")
    assert all(getattr(first, field) is first.call_model for field in fields)
    assert first.backup_plan_model is None
    passed("constructor stores client and shares text adapter without making requests")

    second = ns["GPTResearcher"]("RAG 局限", "web", "research_report", chat_model=model)
    assert first.context is not second.context
    assert first.research_sources is not second.research_sources
    assert first.visited_urls is not second.visited_urls
    passed("shared model client does not implicitly share research state")

    legacy = ns["GPTResearcher"]("RAG", "web", "research_report")
    assert legacy.chat_model is None
    assert legacy.call_model is ns["demo_model"]
    assert legacy.backup_plan_model is ns["demo_backup_plan_model"]
    passed("omitted client preserves the existing demo behavior")

    # Injection must remain effective even if every default callback becomes unusable.
    async def forbidden_default(messages):
        raise AssertionError("An injected report used a default/demo model callback")

    for name in ("demo_model", "demo_plan_model", "demo_write_model",
                 "demo_subtopic_model", "demo_backup_plan_model",
                 "demo_deep_plan_model", "demo_deep_query_model", "demo_deep_extract_model"):
        ns[name] = forbidden_default

    before = len(fixture.researchers)
    ordinary_model = InjectedModel(callbacks, fixture)
    report, owner = await ns["run_agent"](
        "RAG", "web", "research_report", return_researcher=True,
        chat_model=ordinary_model,
    )
    assert len(fixture.researchers) == before + 1
    assert owner.chat_model is ordinary_model
    assert {"role", "plan", "write"} <= set(ordinary_model.stages)
    assert "## 资料来源" in report and owner.research_sources and owner.context
    passed("ordinary entry reaches injected client for role, query planning and writing")

    before = len(fixture.researchers)
    detailed_model = InjectedModel(callbacks, fixture)
    report, parent = await ns["run_agent"](
        "RAG", "web", "detailed_report", return_researcher=True,
        chat_model=detailed_model,
    )
    researchers = fixture.researchers[before:]
    children = [r for r in researchers if r.report_type == "subtopic_report"]
    assert len(children) == 2 and len(researchers) == 3
    assert all(r.chat_model is detailed_model for r in researchers)
    assert {"role", "plan", "subtopics", "write"} <= set(detailed_model.stages)
    assert "## RAG 的工作原理" in report and "## RAG 的局限与改进" in report
    assert report.count("## 资料来源") == 1
    passed("detailed parent, chapter planning and both child researchers use supplied model")

    assert all(c.visited_urls is parent.visited_urls for c in children)
    assert all(c.context is not parent.context for c in children)
    assert children[0].context is not children[1].context
    assert all(c.write_model is parent.write_model for c in children)
    assert not fixture.exports
    assert PRACTICE.read_bytes() == raw
    passed("chapter visited URLs are intentionally shared; contexts remain distinct")
    print(f"\n{len(PASSED)} checks passed; SHA256={hashlib.sha256(raw).hexdigest()}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
