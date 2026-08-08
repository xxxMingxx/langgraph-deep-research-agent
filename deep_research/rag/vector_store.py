from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_PATH = "./chroma_db"


def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5"
    )


def get_vector_store():

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    return vector_store


def search_documents(query: str, k: int = 3):

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results