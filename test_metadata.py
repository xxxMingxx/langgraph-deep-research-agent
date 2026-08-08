from deep_research.rag.vector_store import get_vector_store


db = get_vector_store()


results = db.similarity_search(
    "LangGraph是什么？",
    k=1
)


for doc in results:
    print("====================")
    print(doc.page_content[:300])
    print("metadata:")
    print(doc.metadata)