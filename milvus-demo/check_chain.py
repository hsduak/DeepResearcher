"""Verify saved practice code against real Milvus without model keys or web search.

The deterministic Embedding and planner are test doubles. PDF parsing, splitting,
Milvus storage/search, context formatting, and report assembly use real code.
"""

import ast
import asyncio
import hashlib
import json
import tempfile
import uuid
from pathlib import Path
from types import MethodType, SimpleNamespace

import fitz
from langchain_classic.retrievers.document_compressors import EmbeddingsFilter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_milvus import Milvus
from langchain_text_splitters import RecursiveCharacterTextSplitter


PRACTICE = Path(r"D:\桌面\新建文件夹\1.py")


class TestEmbeddings(Embeddings):
    """Six-dimensional word counts, for integration checks rather than quality."""

    def __init__(self):
        self.document_calls = []
        self.query_calls = []

    def _vector(self, text):
        text = text.lower()
        return [
            float(text.count(term)) + 0.01
            for term in ("rag", "evidence", "retrieval", "milvus", "vector", "database")
        ]

    def embed_documents(self, texts):
        self.document_calls.append(len(texts))
        return [self._vector(text) for text in texts]

    def embed_query(self, text):
        self.query_calls.append(text)
        return self._vector(text)

    async def aembed_query(self, text):
        return self.embed_query(text)


async def unexpected_external_call(*args, **kwargs):
    raise AssertionError("Unexpected model or web-search call")


async def planned_queries(self, query):
    return ["RAG evidence retrieval", "Milvus vector database"]


def write_pdf(path):
    with fitz.open() as pdf:
        for sentence in (
            "RAG retrieves external evidence. Retrieval grounds an answer in evidence.",
            "Milvus is a vector database. A vector index supports database retrieval.",
        ):
            page = pdf.new_page()
            remaining = page.insert_textbox(
                fitz.Rect(40, 40, 555, 800), "\n".join([sentence] * 22), fontsize=10
            )
            assert remaining >= 0, "Test text must fit on its page"
        pdf.save(path)


async def check():
    original = PRACTICE.read_bytes()
    source = original.decode("utf-8-sig")
    compile(source, str(PRACTICE), "exec")
    tree = ast.parse(source)
    names = {
        "DocumentLoader", "ContextManager", "VectorStoreWrapper",
        "ResearcherConductor", "ReportGenerator", "GPTResearcher",
    }
    nodes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name in names]
    assert {n.name for n in nodes} == names
    embeddings = TestEmbeddings()
    collection = "study_check_" + uuid.uuid4().hex
    stores = []

    def create_milvus(**kwargs):
        kwargs["collection_name"] = collection
        store = Milvus(**kwargs)
        stores.append(store)
        return store

    namespace = {
        "asyncio": asyncio, "json": json, "Path": Path,
        "Document": Document, "PyMuPDFLoader": PyMuPDFLoader,
        "RecursiveCharacterTextSplitter": RecursiveCharacterTextSplitter,
        "EmbeddingsFilter": EmbeddingsFilter,
        "Memory": lambda **kwargs: SimpleNamespace(get_embeddings=lambda: embeddings),
        "BrowserManager": lambda **kwargs: SimpleNamespace(**kwargs),
        "Milvus": create_milvus,
        **{name: unexpected_external_call for name in (
            "demo_model", "search_web", "demo_plan_model", "demo_backup_plan_model",
        )},
    }
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(PRACTICE), "exec"), namespace)
    Researcher = namespace["GPTResearcher"]
    query = "Explain RAG evidence retrieval and Milvus vector database"

    def prepare(researcher):
        researcher.agent = "test"
        researcher.role = "test"
        researcher.researcher_conductor.plan_research = MethodType(
            planned_queries, researcher.researcher_conductor
        )

    try:
        with tempfile.TemporaryDirectory(prefix="project2-milvus-") as directory:
            path = Path(directory) / "rag-evidence.pdf"
            write_pdf(path)
            researcher = Researcher(query, "langchain_vectorstore", "research_report")
            prepare(researcher)
            pages = await researcher.load_documents([str(path)])
            assert pages == 2
            assert len(embeddings.document_calls) == 1
            assert embeddings.document_calls[0] > 2, "PDF should produce multiple chunks"
            store = stores[0]

            await asyncio.to_thread(researcher.vector_store.load, [{
                "raw_content": "RAG evidence retrieval " * 20,
                "url": "unrelated-source.txt", "title": "unrelated-source.txt",
            }])
            count_before = store.client.query(
                collection, filter="", output_fields=["count(*)"]
            )[0]["count(*)"]

            contexts = await researcher.conduct_research()
            assert len(contexts) == 3
            assert all(isinstance(context, str) and context for context in contexts)
            assert all(str(path) in context for context in contexts)
            assert all("unrelated-source.txt" not in context for context in contexts)
            report = await researcher.write_report()
            assert report.startswith("# " + query)
            assert "RAG" in report and "Milvus" in report
            assert len(embeddings.query_calls) == 3

            empty = await researcher.context_manager.get_similar_content_by_query_with_vectorstore(
                "RAG", researcher.vector_store, filter='title == "missing.pdf"'
            )
            assert empty == ""
            count_after = store.client.query(
                collection, filter="", output_fields=["count(*)"]
            )[0]["count(*)"]
            assert count_after == count_before, "Research must not repeat ingestion"
            assert len(embeddings.document_calls) == 2
            print("PASS: real PDF -> chunks -> Milvus -> three queries -> context -> report")
            print("PASS: source filter / empty results / no repeated ingestion")

            for mode in ("local", "hybrid"):
                local = Researcher(query, mode, "research_report")
                prepare(local)
                local.cfg["doc_paths"] = [str(path)]

                async def local_web_material(self, subquery):
                    return [{
                        "raw_content": "Simulated web evidence for " + subquery,
                        "url": "https://example.invalid/evidence", "title": "Web example",
                    }]

                local.researcher_conductor._scrape_data_by_urls = MethodType(
                    local_web_material, local.researcher_conductor
                )
                local_contexts = await local.conduct_research()
                assert local_contexts and all(isinstance(c, str) for c in local_contexts)
                if mode == "hybrid":
                    assert len(local_contexts) == 2
                    assert local_contexts[0].startswith("本地资料：")
                    assert local_contexts[1].startswith("网页资料：")
            print("PASS: local and hybrid paths after loader/formatting fixes")
            assert PRACTICE.read_bytes() == original
            print("PDF pages:", pages, "| stored rows:", count_after)
            print("Saved practice SHA256:", hashlib.sha256(original).hexdigest())
    finally:
        for store in stores:
            # Delete only this run's newly generated test collection.
            assert collection.startswith("study_check_")
            if store.client.has_collection(collection):
                store.client.drop_collection(collection)
            if store._async_milvus_client is not None:
                await store.aclient.close()
            store.client.close()
        print("Temporary test collection cleaned up:", collection)


if __name__ == "__main__":
    asyncio.run(check())
