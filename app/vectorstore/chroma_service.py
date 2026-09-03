from langchain_chroma import Chroma

from app.services.embedding_service import get_embedding_model


COLLECTION_NAME = "devops_documents"
PERSIST_DIRECTORY = "chroma_data"


def get_vectorstore():

    embeddings = get_embedding_model()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vectorstore
