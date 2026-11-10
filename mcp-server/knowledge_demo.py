"""Read-only, fictional knowledge base for the chapter 10 MCP exercise."""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("knowledge")

DOCUMENTS = {
    "doc_1": {
        "title": "报销规定",
        "content": "演示规定：报销需要提供发票，并由主管审批。",
    },
}


@mcp.tool()
def search_docs(query: str) -> list[dict]:
    """按关键词搜索文档，返回文档编号和标题。"""
    return [
        {"doc_id": doc_id, "title": document["title"]}
        for doc_id, document in DOCUMENTS.items()
        if query in document["title"]
    ]


@mcp.tool()
def read_doc(doc_id: str) -> dict:
    """根据文档编号读取文档正文。"""
    if doc_id not in DOCUMENTS:
        raise ValueError(f"文档不存在：{doc_id}")
    return DOCUMENTS[doc_id]


if __name__ == "__main__":
    mcp.run(transport="stdio")
