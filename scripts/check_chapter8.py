"""Verify the saved LangGraph exercise without keys or external services.

Loads actual saved definitions through the chapter-six AST loader. Full graph
and HTTP cases retain actual GPTResearcher orchestration and document filtering;
external models/search/scrape/Embedding/exports are deterministic doubles.
Control-flow cases replace research I/O only, retaining all saved team nodes.
"""

import asyncio
from collections import Counter
import hashlib
import json
import re

from fastapi.testclient import TestClient

from check_chapter6 import Fixture, PRACTICE, expect_error, load_practice


CHECKS = []
ORIGINAL = PRACTICE.read_bytes()


def passed(name):
    CHECKS.append(name)
    print(f"PASS {len(CHECKS):02d}: {name}", flush=True)


class TeamFixture(Fixture):
    def __init__(self, ns):
        super().__init__(ns)
        self.calls = Counter()
        self.reviews = Counter()
        self.prompts = []
        self.accepted = []
        self.always_review = False
        self.always_fact = False
        self.review_once = True
        self.fact_once = True
        self.extra_section = False
        self.overrides = {}
        self.diagram = "```mermaid\nflowchart LR\n A[None] --> B[Evidence]\n```"

    async def model(self, messages):
        system, user = messages[0]["content"], messages[-1]["content"]
        if "研究编辑" in system:
            role = "planner"
        elif "审阅者" in system:
            role = "reviewer"
        elif "草稿修改" in system or "报告修改者" in system:
            role = "reviser"
        elif "报告撰写者" in system:
            role = "writer"
        elif "事实审查者" in system:
            role = "fact"
        elif "Mermaid" in system:
            role = "visualizer"
        else:
            raise AssertionError(f"Unknown team role: {system}")
        self.calls[role] += 1
        self.prompts.append((role, user))
        if role in self.overrides:
            return self.overrides[role]
        if role == "planner":
            assert "初始研究报告" in user
            sections = ["RAG 原理", "部署成本"]
            if self.extra_section and "加上证据评估" in user:
                sections.append("证据评估")
            return json.dumps({"title": "RAG 团队报告", "sections": sections}, ensure_ascii=False)
        if role in ("reviewer", "reviser"):
            match = re.search(r"当前章节：([^\n]+)", user)
            assert match, user
            topic = match.group(1)
            if role == "reviewer":
                self.reviews[topic] += 1
                if self.always_review or (self.review_once and topic == "RAG 原理" and self.reviews[topic] == 1):
                    return "补充检索证据的局限。"
                self.accepted.append(topic)
                return "None"
            assert "补充检索证据的局限" in user
            return json.dumps({
                "draft": {topic: f"## {topic}\n\nCHAPTER_REVISED：检索证据有局限。[证据](https://fixture.invalid/shared)"},
                "revision_notes": "补充了检索证据的局限。",
            }, ensure_ascii=False)
        if role == "writer":
            if self.calls[role] > 1:
                assert "引言措辞需要收敛" in user
            return json.dumps({
                "introduction": f"INTRO-v{self.calls[role]}：本文讨论 RAG 落地。",
                "table_of_contents": "- RAG 原理\n- 部署成本",
                "conclusion": "CONCLUSION：应关注证据质量与成本。",
                "sources": ["[测试证据](https://fixture.invalid/shared)"],
                "research_data": [{"injected": "MUST_NOT_OVERWRITE"}],
            }, ensure_ascii=False)
        if role == "fact":
            if self.always_fact or (self.fact_once and self.calls[role] == 1):
                return "引言措辞需要收敛。"
            return "None"
        return self.diagram


def fresh(fast=False):
    raw, ns = load_practice()
    assert raw == ORIGINAL, "Saved exercise changed during verification"
    fixture = TeamFixture(ns)
    if fast:
        async def research(self, query, source="web", report_type="research_report", parent_query=""):
            await asyncio.sleep(0)
            return f"## {query}\n\nRAG 需要检索证据。[证据](https://fixture.invalid/shared)"
        ns["ResearchAgent"].research = research
    return ns, fixture


async def full_graph():
    ns, fixture = fresh()
    async def no_feedback(sections):
        raise AssertionError("Disabled feedback must not be called")
    result = await ns["run_multi_agent_task"]("RAG 如何落地", fixture.model, ask_feedback=no_feedback)
    assert result["report"].startswith("# RAG 团队报告")
    assert [next(iter(d)) for d in result["research_data"]] == ["RAG 原理", "部署成本"]
    assert "CHAPTER_REVISED" in result["research_data"][0]["RAG 原理"]
    assert result["human_feedback"] is None and result["plan_revision_count"] == 0
    assert result["fact_check_notes"] is None and result["fact_check_revision_count"] == 1
    assert "INTRO-v2" in result["report"] and "A[None]" in result["report"]
    assert "MUST_NOT_OVERWRITE" not in result["report"]
    assert fixture.calls == Counter(planner=1, reviewer=3, reviser=1, writer=2, fact=2, visualizer=1), fixture.calls
    assert len(fixture.researchers) == 3 and fixture.scraped
    chapter_prompts = [user for _, user, _ in fixture.writes if "本次只撰写当前章节正文" in user]
    assert len(chapter_prompts) == 2 and all("RAG 如何落地" in user for user in chapter_prompts)
    assert fixture.exports == []
    passed("Saved full graph runs actual research/document pipeline, chapter revision, fact retry and publication")
    assert fixture.reviews == Counter({"RAG 原理": 2, "部署成本": 1})
    assert fixture.accepted[0] == "部署成本"
    passed("Parallel chapters retain input order; only the first chapter is revised; Writer preserves chapter bodies")


async def human_paths():
    ns, fixture = fresh(fast=True)
    fixture.extra_section = True
    answers = iter(["加上证据评估", "no"])
    plans = []
    async def feedback(sections):
        plans.append(list(sections))
        return next(answers)
    result = await ns["run_multi_agent_task"]("RAG", fixture.model, include_human_feedback=True, ask_feedback=feedback)
    assert fixture.calls["planner"] == 2 and len(plans[0]) == 2 and len(plans[1]) == 3
    assert result["sections"][-1] == "证据评估" and result["plan_revision_count"] == 1
    passed("Human feedback reaches replanning; no accepts the new plan without increasing the count")
    async def critical(sections):
        return "not enough evidence"
    human = ns["HumanAgent"](critical)
    update = await human.review_plan({"task": {"include_human_feedback": True}, "sections": ["A"]})
    assert update["human_feedback"] == "not enough evidence" and update["plan_revision_count"] == 1
    passed("Human approval checks a whole no token instead of swallowing critical notes")
    ns, fixture = fresh(fast=True)
    async def always(sections):
        return "加上证据评估"
    await expect_error(RuntimeError, ns["run_multi_agent_task"]("RAG", fixture.model, include_human_feedback=True, ask_feedback=always))
    assert fixture.calls["planner"] == 4 and fixture.calls["writer"] == 0
    passed("Fourth human modification request stops before chapter research/writing")


async def revision_limits():
    ns, fixture = fresh(fast=True)
    fixture.always_review = True
    await expect_error(RuntimeError, ns["run_multi_agent_task"]("RAG", fixture.model))
    # gather propagates the error; let any sibling finish before examining counts.
    await asyncio.sleep(0)
    assert fixture.reviews == Counter({"RAG 原理": 4, "部署成本": 4}), fixture.reviews
    assert fixture.calls["reviser"] == 6 and fixture.calls["writer"] == 0
    passed("Chapter limit permits three rewrites per chapter and propagates continued failure")
    ns, fixture = fresh(fast=True)
    fixture.always_fact = True
    await expect_error(RuntimeError, ns["run_multi_agent_task"]("RAG", fixture.model))
    assert fixture.calls["writer"] == 4 and fixture.calls["fact"] == 4 and fixture.calls["visualizer"] == 0
    passed("Fact loop stops after three rewrites and never publishes unaccepted work")


async def invalid_outputs():
    ns, fixture = fresh(fast=True)
    plan_state = {"task": {"query": "RAG"}, "initial_research": "RAG 背景"}
    for output in ("not JSON", "[]", '{"title":"T","sections":[]}', '{"title":"T","sections":[1]}'):
        fixture.overrides["planner"] = output
        await expect_error(ValueError, ns["EditorAgent"](fixture.model).plan_research(plan_state))
    fixture.overrides["planner"] = json.dumps({"title": "T", "sections": ["A", "B", "C", "D"]})
    assert len((await ns["EditorAgent"](fixture.model).plan_research(plan_state))["sections"]) == 3
    await expect_error(ValueError, ns["EditorAgent"](fixture.model).plan_research(dict(plan_state, task={"query": "RAG", "max_sections": 0})))
    passed("Planner rejects malformed structures and zero limits; code enforces the section cap")
    draft_state = {"task": {"query": "RAG"}, "topic": "A", "draft": {"A": "body"}}
    for role, cls in (("reviewer", "ReviewerAgent"), ("fact", "FactCheckerAgent"), ("visualizer", "VisualizerAgent")):
        state = draft_state if role == "reviewer" else {"introduction": "I", "research_data": [], "conclusion": "C"}
        for output in (None, "", "  ", 42):
            fixture.overrides[role] = output
            await expect_error(ValueError, ns[cls](fixture.model).run(state))
    passed("Empty/wrong-type model failures never become reviewer/fact acceptance or an absent diagram")
    fixture.overrides["reviewer"] = "None of the criteria are satisfied."
    review = await ns["ReviewerAgent"](fixture.model).run(draft_state)
    assert review["review"].startswith("None of") and review["draft_revision_count"] == 1
    fixture.overrides["reviewer"] = " NoNe "
    assert (await ns["ReviewerAgent"](fixture.model).run(dict(draft_state, draft_revision_count=2)))["draft_revision_count"] == 2
    passed("Exact acceptance tokens preserve real issues and do not increment approved review counts")
    for output in ("[]", '{"draft":[]}', '{"draft":{"wrong":"body"},"revision_notes":"x"}', '{"draft":{"A":"body"},"revision_notes":""}'):
        fixture.overrides["reviser"] = output
        await expect_error(ValueError, ns["ReviserAgent"](fixture.model).run(dict(draft_state, review="change")))
    await expect_error(ValueError, ns["ReviserAgent"](fixture.model).run(dict(draft_state, review=None)))
    passed("Reviser requires a valid full draft under the current topic and meaningful revision notes")
    writer_state = {"task": {"query": "RAG"}, "title": "T", "research_data": [{"A": "body"}]}
    for output in ("[]", '{}', '{"introduction":"I","table_of_contents":"T","conclusion":"C","sources":"bad"}'):
        fixture.overrides["writer"] = output
        await expect_error(ValueError, ns["WriterAgent"](fixture.model).run(writer_state))
    passed("Writer rejects missing fields and invalid source containers before publication")
    ns, fixture = fresh(fast=True)
    fixture.diagram = "None"
    result = await ns["run_multi_agent_task"]("RAG", fixture.model)
    assert result["diagrams"] == [] and "## 图表" not in result["report"]
    passed("No-diagram response still produces a complete report without an empty diagram section")


def http_paths():
    ns, fixture = fresh()
    with TestClient(ns["app"], raise_server_exceptions=False) as client:
        before = len(fixture.researchers)
        assert client.post("/report/", json={"task": "RAG", "report_type": "multi_agents"}).status_code == 503
        assert len(fixture.researchers) == before and fixture.exports == []
        assert client.post("/report/", json={}).status_code == 422
        passed("HTTP unconfigured model gives 503 without research/export; missing task gives 422")
        ns["app"].state.team_model = fixture.model
        response = client.post("/report/", json={"task": "RAG", "report_type": "multi_agents"})
        assert response.status_code == 200, response.text
        result = response.json()
        info = result["researcher_information"]
        assert info["source_urls"] is None and info["research_costs"] is None and info["references"]
        assert result["docx_path"] == "outputs/fixture.docx" and result["pdf_path"] == "outputs/fixture.pdf"
        assert fixture.exports[-2][0] == "word" and fixture.exports[-1][0] == "pdf"
        assert fixture.exports[-2][1] == result["report"] == fixture.exports[-1][1]
        assert len(fixture.researchers) == 3
        passed("HTTP multi_agents executes the saved full graph and exports the identical final report")
        fixture.overrides["planner"] = "not JSON"
        before = len(fixture.exports)
        response = client.post("/report/", json={"task": "RAG", "report_type": "multi_agents"})
        assert response.status_code == 500 and len(fixture.exports) == before
        passed("Graph/model failure surfaces as HTTP 500 and never exports a false-success report")


async def check_async():
    await full_graph()
    await human_paths()
    await revision_limits()
    await invalid_outputs()


def main():
    _, ns = load_practice()
    fixture = TeamFixture(ns)
    chief = ns["ChiefEditorAgent"]({"query": "RAG"}, fixture.model)
    chief._create_workflow().compile()
    chief.editor._create_draft_workflow().compile()
    passed("Saved file and both graphs compile with the actual state schemas and node references")
    asyncio.run(check_async())
    http_paths()
    assert PRACTICE.read_bytes() == ORIGINAL, "Exercise changed during verification"
    print(f"\n{len(CHECKS)} chapter-eight checks passed. No real model, services or exports used.")
    print("Practice SHA256:", hashlib.sha256(ORIGINAL).hexdigest())


if __name__ == "__main__":
    main()
