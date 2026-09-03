from app.utils.document_loader import (
    load_documents,
    split_documents
)


def test_documents_loaded():

    documents = load_documents()

    assert len(documents) > 0


def test_documents_split():

    documents = load_documents()

    chunks = split_documents(documents)

    assert len(chunks) > 0
