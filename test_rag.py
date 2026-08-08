from deep_research.rag.ingestion import build_vector_store
from deep_research.rag.vector_store import search_documents


docs = [
    """
    LangGraph is a framework for building stateful multi-agent applications.
    """,

    """
    RAG combines retrieval and generation using vector databases.
    """,

    """
    Deep Research Agent can use tools and multiple agents to solve complex tasks.
    """
]


# 创建向量数据库
build_vector_store(docs)


# 查询
results = search_documents(
    "What is LangGraph?",
    k=2
)


for r in results:
    print("================")
    print(r.page_content)