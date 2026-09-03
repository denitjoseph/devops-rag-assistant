import sys
from pathlib import Path

# Add project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.utils.document_loader import (
    load_documents,
    split_documents
)

from app.vectorstore.chroma_service import (
    get_vectorstore
)


def ingest_documents():

    print("Loading documents...")

    documents = load_documents()

    print(f"Documents loaded: {len(documents)}")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    print("Connecting to ChromaDB...")

    vectorstore = get_vectorstore()

    print("Adding documents to ChromaDB...")

    vectorstore.add_documents(chunks)

    print("Documents successfully added to ChromaDB.")


if __name__ == "__main__":
    ingest_documents()
