from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter


DOCUMENTS_PATH = Path("documents")


def load_documents():

    loader = DirectoryLoader(
        str(DOCUMENTS_PATH),
        glob="**/*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    return documents


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
