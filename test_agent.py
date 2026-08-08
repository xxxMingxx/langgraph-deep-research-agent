from deep_research.agents.research_agent import researcher_agent


result = researcher_agent.invoke(
    {
        "research_topic": """
请根据本地知识库中的资料，
分析 LangGraph 和 RAG 在 Deep Research Agent 项目中的作用。
如果知识库中存在相关信息，请优先使用 chroma_search。
""",
        "researcher_messages": []
    }
)


print("====================")
print(result)

print("====================")
print(result["compressed_research"])