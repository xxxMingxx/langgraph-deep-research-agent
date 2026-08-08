from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os

VECTOR_DB_PATH = "./chroma_db"
KNOWLEDGE_PATH = "./knowledge_base"

def build_vector_store(texts):

    documents = [
    Document(
        page_content=t["content"],
        metadata={
            "source": t["source"],
            "category": t.get("category", "general")
        }
    )
    for t in texts
]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = splitter.split_documents(
        documents
    )


    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5"
    )


    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=VECTOR_DB_PATH
    )


    return db



if __name__ == "__main__":

    docs = []


for filename in os.listdir(KNOWLEDGE_PATH):

    filepath = os.path.join(
        KNOWLEDGE_PATH,
        filename
    )

    if filename.endswith(".md"):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            docs.append(
                {
                    "content": f.read(),
                    "source": filename,
                    "category": "knowledge_base"
                }
            )

    build_vector_store(docs)


    print("Knowledge base vector database created!")

    