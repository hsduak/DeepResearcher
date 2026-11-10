"""Verify injected clients reach chapter 7/8/9 research objects at runtime.

Actual saved recursion worker, LangGraph workflow and Deep Agents SDK execute.
All external model/search/scraping/embedding responses remain fixed fixtures.
"""

import asyncio
import hashlib
import os
from pathlib import Path
from tempfile import TemporaryDirectory

os.environ["LANGCHAIN_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

from check_chapter6 import Fixture, PRACTICE, load_practice
from check_chapter8 import TeamFixture
from check_chapter9 import ScriptedResearchModel
from check_chapter10_models import InjectedModel


ROOT = Path(__file__).resolve().parents[1]


def callbacks(ns):
    return {"role": ns["demo_model"], "plan": ns["demo_plan_model"],
            "subtopics": ns["demo_subtopic_model"]}


async def main():
    raw, ns = load_practice()
    fixture = Fixture(ns)
    inner = InjectedModel(callbacks(ns), fixture)
    parent = ns["GPTResearcher"]("RAG", "web", "deep", chat_model=inner)

    async def fixed_extract(query, context):
        assert "Source:" in context
        return {"learnings": ["fixture learning"], "citations": {},
                "followUpQuestions": [], "researchGoal": "fixture goal"}

    parent.deep_researcher.process_research_results = fixed_extract
    result = await parent.deep_researcher._process_query({"query": "RAG 原理", "researchGoal": "G"})
    child = fixture.researchers[-1]
    assert result and child is not parent and child.chat_model is inner
    assert child.visited_urls is parent.visited_urls and {"role", "plan"} <= set(inner.stages)
    print("PASS 01: recursive worker passes parent client to the actual child research object", flush=True)

    _, ns = load_practice()
    team = TeamFixture(ns)
    inner = InjectedModel(callbacks(ns), team)
    state = await ns["run_multi_agent_task"](
        "RAG 如何落地", call_model=team.model, chat_model=inner,
    )
    assert len(team.researchers) == 3
    assert all(r.chat_model is inner for r in team.researchers)
    assert state["report"].startswith("# RAG 团队报告")
    assert [r.report_type for r in team.researchers] == [
        "research_report", "subtopic_report", "subtopic_report",
    ]
    print("PASS 02: actual LangGraph initial and both chapter researchers receive the supplied client", flush=True)

    _, ns = load_practice()
    fixture = Fixture(ns)
    inner = InjectedModel(callbacks(ns), fixture)
    outer = ScriptedResearchModel()
    scratch = ROOT / "outputs" / "chapter10_checks"
    scratch.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix="wiring-", dir=scratch) as tmp:
        result = await ns["run_deep_agent_task"](
            "RAG", model=outer, research_model=inner, run_dir=tmp,
        )
        assert Path(result["report_path"]).is_file() and result["report"].strip()
        assert fixture.researchers and all(r.chat_model is inner for r in fixture.researchers)
        assert {"role", "plan", "write"} <= set(inner.stages)
        assert outer.events
    print("PASS 03: real Deep Agents outer model delegates to tools using a distinct inner research client", flush=True)

    assert PRACTICE.read_bytes() == raw
    print(f"\n3 checks passed; SHA256={hashlib.sha256(raw).hexdigest()}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
