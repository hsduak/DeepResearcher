"""Verify the saved DeepResearch exercise without services or keys.

Reuses the chapter-six AST loader. Actual saved research/writing orchestration,
Document conversion, splitting, filtering and HTTP handlers run. Model, search,
page-fetch, Embedding and export adapters are deterministic test doubles.
"""

import asyncio
import contextlib
import io
import json
import re

from fastapi.testclient import TestClient

from check_chapter6 import Fixture, PRACTICE, expect_error, load_practice


CHECKS = []


def passed(name):
    CHECKS.append(name)
    print(f"PASS {len(CHECKS):02d}: {name}", flush=True)


class DeepFixture(Fixture):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.direction_prompts = []
        self.query_plans = []
        self.extractions = []
        namespace.update({
            "demo_deep_plan_model": self.directions,
            "demo_deep_query_model": self.queries,
            "demo_deep_extract_model": self.extract,
        })

    async def directions(self, messages):
        user = messages[-1]["content"]
        assert "搜索背景：" in user
        self.direction_prompts.append(user)
        return json.dumps({"questions": ["Risk?", "Improvement?"]})

    async def queries(self, messages):
        user = messages[-1]["content"]
        prefix_match = re.search(r"GOAL-([A-Z0-9]+)", user)
        prefix = prefix_match.group(1) if prefix_match else ""
        labels = [prefix + "1", prefix + "2"] if prefix else ["A", "B"]
        self.query_plans.append(prefix or "root")
        return json.dumps([
            {"query": label, "researchGoal": "GOAL-" + label}
            for label in labels
        ])

    async def extract(self, messages):
        user = messages[-1]["content"]
        label = user.splitlines()[0].removeprefix("当前任务：")
        assert "Source:" in user and "Content:" in user
        source = re.search(r"Source: (https?://\S+)", user)
        assert source is not None
        learning = "FACT-" + label
        self.extractions.append(label)
        return json.dumps({
            "learnings": [learning, learning],
            "citations": {learning: source.group(1)},
            "followUpQuestions": ["NEXT-" + label + "?"],
        })


def fresh():
    original, namespace = load_practice()
    return original, namespace, DeepFixture(namespace)


async def returning(value):
    return value


async def check_interfaces():
    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")
    skill = parent.deep_researcher
    assert skill is not None and skill.researcher is parent
    assert ns["GPTResearcher"]("RAG", "web", "research_report").deep_researcher is None
    questions = await skill.generate_research_plan("RAG")
    assert questions == ["Risk?", "Improvement?"]
    assert "RAG" in fixture.direction_prompts[-1]
    parent.deep_plan_model = lambda messages: returning("[]")
    await expect_error(ValueError, skill.generate_research_plan("RAG"))
    parent.deep_plan_model = lambda messages: returning('{"questions": []}')
    assert await skill.generate_research_plan("RAG") == ["RAG"]
    passed("Direction planning receives search context; object validation and fallback work")

    data = [
        None, {"query": 123, "researchGoal": "bad"},
        {"query": " A ", "researchGoal": " GOAL-A "},
        {"query": " ", "researchGoal": "blank"},
        {"query": "B", "researchGoal": "GOAL-B"},
        {"query": "C", "researchGoal": "GOAL-C"},
    ]
    parent.deep_query_model = lambda messages: returning(json.dumps(data))
    assert await skill.generate_search_queries("RAG", 2) == [
        {"query": "A", "researchGoal": "GOAL-A"},
        {"query": "B", "researchGoal": "GOAL-B"},
    ]
    parent.deep_query_model = lambda messages: returning("{}")
    await expect_error(ValueError, skill.generate_search_queries("RAG", 2))
    passed("Task parsing checks every item, trims fields and respects the breadth cap")

    before = len(fixture.extractions)
    await expect_error(ValueError, skill.process_research_results("A", "  "))
    assert len(fixture.extractions) == before
    result = await skill.process_research_results(
        "A", ["Source: https://fixture.invalid/a", "Content: evidence"], 1,
    )
    assert result["learnings"] == ["FACT-A"]
    assert result["citations"] == {"FACT-A": "https://fixture.invalid/a"}
    for invalid in ("[]", '{"learnings": "wrong"}', '{"citations": []}', "not JSON"):
        parent.deep_extract_model = lambda messages, value=invalid: returning(value)
        await expect_error(ValueError, skill.process_research_results("A", "evidence"))
    passed("Extraction normalizes material lists, rejects empty material and checks output containers")


async def check_tree():
    _, ns, fixture = fresh()
    conductor_class = ns["ResearcherConductor"]
    original_conduct = conductor_class.conduct_research

    async def priced_conduct(conductor):
        result = await original_conduct(conductor)
        # A synthetic accounting unit, not a real provider price.
        conductor.researcher.research_costs += 1.0
        return result

    conductor_class.conduct_research = priced_conduct
    report, parent = await ns["run_agent"]("RAG", "web", "deep", True)
    children = fixture.researchers[1:]
    assert parent is fixture.researchers[0]
    assert [child.query for child in children] == ["A", "B", "A1", "A2", "B1", "B2"]
    assert fixture.query_plans == ["root", "A", "B"]
    assert all(child.report_type == "research_report" and child.deep_researcher is None
               for child in children)
    assert isinstance(parent.context, str) and isinstance(parent.visited_urls, set)
    assert all(child.visited_urls is parent.visited_urls for child in children)
    assert parent.get_costs() == 6.0
    assert len(fixture.scraped) == len(set(fixture.scraped))
    assert len(parent.get_source_urls()) == len(set(fixture.scraped))
    assert len(fixture.writes) == 1, "Only the parent writes the final report"
    writing_prompt = fixture.writes[0][1]
    for label in ("A", "B", "A1", "A2", "B1", "B2"):
        marker = f"FACT-{label} [Source:"
        assert parent.context.count(marker) == 1
        assert marker in writing_prompt
    assert report.count("## 资料来源") == 1
    passed("Two-level end-to-end flow runs six ordinary children, then writes once")
    passed("Parent/children share the same empty-origin URL set and reuse collected source state")
    passed("Recorded child accounting units sum once; cited discoveries reach final writing")


async def check_depth_counts():
    for depth, expected in ((1, 2), (2, 6), (3, 14)):
        _, ns, _ = fresh()
        skill = ns["GPTResearcher"]("RAG", "web", "deep").deep_researcher
        seen = []

        async def node(task):
            seen.append(task["query"])
            return {
                "learnings": ["L-" + task["query"]], "citations": {},
                "visited_urls": [], "context": "C-" + task["query"], "sources": [],
                "researchGoal": task["researchGoal"], "followUpQuestions": ["next?"],
            }

        skill._process_query = node
        result = await skill.deep_research("root", 2, depth)
        assert len(seen) == expected and len(result["learnings"]) == expected
        assert len(result["context"]) == expected
    passed("Recursion stops at the correct depth: 2 / 6 / 14 nodes without historical duplication")


async def check_stops():
    _, ns, fixture = fresh()
    skill = ns["GPTResearcher"]("RAG", "web", "deep").deep_researcher
    for breadth, depth in ((0, 2), (2, 0)):
        result = await skill.deep_research("root", breadth, depth)
        assert result["learnings"] == [] and result["visited_urls"] == set()
    assert fixture.query_plans == []
    skill.researcher.deep_query_model = lambda messages: returning("[]")
    result = await skill.deep_research("root", 2, 3)
    assert result["context"] == [] and len(fixture.researchers) == 1
    passed("Zero work allowances and empty task plans safely return initialized results")

    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")

    async def fail_extract(messages):
        raise RuntimeError("fixture extraction failure")

    parent.deep_extract_model = fail_extract
    with contextlib.redirect_stdout(io.StringIO()):
        context = await parent.conduct_research()
    assert context == "" and fixture.query_plans == ["root"]
    assert len(fixture.researchers) == 3
    assert parent.research_sources, "Collected material can remain after extraction fails"
    await expect_error(ValueError, parent.write_report())
    passed("All failed nodes stop descent; an empty final context prevents report generation")

    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")

    async def fail_a(messages):
        if messages[-1]["content"].splitlines()[0] == "当前任务：A":
            raise RuntimeError("fixture branch A fails")
        return await fixture.extract(messages)

    parent.deep_extract_model = fail_a
    with contextlib.redirect_stdout(io.StringIO()):
        context = await parent.conduct_research()
    assert fixture.query_plans == ["root", "B"]
    assert [r.query for r in fixture.researchers[1:]] == ["A", "B", "B1", "B2"]
    assert "FACT-A [Source:" not in context and "FACT-B2 [Source:" in context
    passed("A failed branch is skipped while its successful sibling continues recursively")


async def check_semaphore():
    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")
    first_entered = asyncio.Event()
    another_entered = asyncio.Event()
    active = 0
    peak = 0
    finished = []

    async def three_tasks(messages):
        return json.dumps([{"query": q, "researchGoal": "GOAL-" + q} for q in ("A", "B", "C")])

    async def blocked_extract(messages):
        nonlocal active, peak
        label = messages[-1]["content"].splitlines()[0].removeprefix("当前任务：")
        if label != "A":
            await first_entered.wait()
        active += 1
        peak = max(peak, active)
        try:
            if label == "A":
                first_entered.set()
                await another_entered.wait()
            else:
                another_entered.set()
            await asyncio.sleep(0)
            result = await fixture.extract(messages)
            finished.append(label)
            return result
        finally:
            active -= 1

    parent.deep_query_model = three_tasks
    parent.deep_extract_model = blocked_extract
    result = await asyncio.wait_for(parent.deep_researcher.deep_research("root", 3, 1), 10)
    assert peak == 2 and active == 0
    assert set(finished) == {"A", "B", "C"}
    assert result["learnings"] == [item for q in ("A", "B", "C") for item in ["FACT-" + q] * 2]
    passed("Three nodes obey the two-permit limit through extraction; gather preserves input ordering")


async def check_cost_and_cancel():
    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")
    conductor = ns["ResearcherConductor"]
    original = conductor.conduct_research

    async def billed_failure(instance):
        instance.researcher.research_costs = 3.0
        raise RuntimeError("fixture failure after recording cost")

    conductor.conduct_research = billed_failure
    with contextlib.redirect_stdout(io.StringIO()):
        result = await parent.deep_researcher._process_query({"query": "F", "researchGoal": "G"})
    assert result is None and parent.get_costs() == 3.0
    conductor.conduct_research = original
    assert await parent.deep_researcher._process_query({"query": "OK", "researchGoal": "G"})
    passed("Failed child accounting is collected in finally and its permit is released")

    started = asyncio.Event()
    never = asyncio.Event()
    parent.deep_researcher.semaphore = asyncio.Semaphore(1)

    async def wait_forever(messages):
        started.set()
        await never.wait()

    parent.deep_extract_model = wait_forever
    task = asyncio.create_task(parent.deep_researcher._process_query({"query": "CANCEL", "researchGoal": "G"}))
    await asyncio.wait_for(started.wait(), 10)
    task.cancel()
    await expect_error(asyncio.CancelledError, task)
    parent.deep_extract_model = fixture.extract
    assert await asyncio.wait_for(parent.deep_researcher._process_query({"query": "AFTER", "researchGoal": "G"}), 10)
    passed("Cancellation propagates and releases the shared permit for subsequent work")


async def check_completed_cache():
    _, ns, fixture = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")
    url = "https://fixture.invalid/completed-cache"

    async def cached_search(query):
        return [{"url": url}]

    parent.search = cached_search
    parent.visited_urls.add(url)
    parent.research_sources.append({"url": url, "raw_content": "RAG evidence. " * 20})
    original_set = parent.visited_urls
    context = await parent.conduct_research()
    assert len(fixture.extractions) == 6 and "FACT-B2" in context
    assert fixture.scraped == [] and len(parent.research_sources) == 1
    assert parent.visited_urls is original_set and isinstance(original_set, set)
    passed("Completed cached material serves all six nodes with no new scraping or set replacement")


async def check_inflight_boundary():
    _, ns, _ = fresh()
    parent = ns["GPTResearcher"]("RAG", "web", "deep")
    claimed = asyncio.Event()
    release_fetch = asyncio.Event()
    url = "https://fixture.invalid/pending"

    class PendingChild:
        def __init__(self, **kwargs):
            self.query = kwargs["query"]
            self.visited_urls = set()
            self.research_sources = []

        async def conduct_research(self):
            if self.query == "A":
                self.visited_urls.add(url)
                claimed.set()
                await release_fetch.wait()
                self.research_sources.append({"url": url, "raw_content": "RAG evidence. " * 20})
            else:
                await claimed.wait()
                assert url in self.visited_urls
            return []

        def get_costs(self):
            return 0.0

    ns["GPTResearcher"] = PendingChild
    first = asyncio.create_task(parent.deep_researcher._process_query({"query": "A", "researchGoal": "G-A"}))
    try:
        await asyncio.wait_for(claimed.wait(), 10)
        with contextlib.redirect_stdout(io.StringIO()):
            sibling = await asyncio.wait_for(parent.deep_researcher._process_query({"query": "B", "researchGoal": "G-B"}), 10)
        assert sibling is None and parent.research_sources == []
    finally:
        release_fetch.set()
        completed = await asyncio.wait_for(first, 10)
    assert completed and len(parent.research_sources) == 1
    passed("Known boundary: an in-flight URL claim cannot yet supply completed material to a sibling")


def check_trim():
    _, ns, _ = fresh()
    trim = ns["trim_context_to_word_limit"]
    assert trim(["early text", "new text"], 2) == ["new text"]
    assert trim(["one two three four"], 2) == ["one two"]
    assert trim(["text"], 0) == []
    assert trim(["raw body tail", "finding source"], 3) == ["finding source"]
    assert trim(["无空格中文" * 100], 1) == ["无空格中文" * 100]
    passed("Whitespace trimming keeps later discoveries, handles oversized tails and has known Chinese limits")


def check_http():
    _, ns, fixture = fresh()
    with TestClient(ns["app"], raise_server_exceptions=False) as client:
        response = client.post("/report/", json={"task": "RAG", "report_type": "deep"})
        assert response.status_code == 200, response.text
        result = response.json()
        assert result["report"] and result["researcher_information"]["source_urls"]
        assert result["docx_path"] == "outputs/fixture.docx"
        assert result["pdf_path"] == "outputs/fixture.pdf"
        assert fixture.exports[-2][1] == result["report"] == fixture.exports[-1][1]
        assert len(fixture.researchers) == 7
        assert client.post("/report/", json={}).status_code == 422
        assert client.post("/report/", json={"task": "RAG", "report_type": "multi_agents"}).status_code == 503
        passed("HTTP deep requests reach final report/export adapters; 422/503 branches remain distinct")

        async def broken_plan(messages):
            return "not JSON"

        ns["demo_deep_query_model"] = broken_plan
        before = len(fixture.exports)
        failed = client.post("/report/", json={"task": "RAG", "report_type": "deep"})
        assert failed.status_code == 500 and len(fixture.exports) == before
        passed("Task-planning errors propagate as HTTP failure instead of exporting a false success")


async def check_async():
    await check_interfaces()
    await check_tree()
    await check_depth_counts()
    await check_stops()
    await check_semaphore()
    await check_cost_and_cancel()
    await check_completed_cache()
    await check_inflight_boundary()


def main():
    original = PRACTICE.read_bytes()
    asyncio.run(check_async())
    check_trim()
    check_http()
    assert PRACTICE.read_bytes() == original, "Practice changed during verification"
    print(f"\n{len(CHECKS)} chapter-seven checks passed. No external services or real exports called.")


if __name__ == "__main__":
    main()
