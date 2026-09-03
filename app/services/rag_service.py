from app.vectorstore.chroma_service import get_vectorstore
from app.services.llm_service import get_llm


def ask_question(question):

    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(
        question,
        k=3
    )

    if not results:
        return {
            "answer": "I could not find relevant information in the documentation.",
            "sources": []
        }

    context_parts = []

    sources = []

    for document in results:

        context_parts.append(
            document.page_content
        )

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        if source not in sources:
            sources.append(source)

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a DevOps AI Assistant.

Answer the user's question using ONLY the provided documentation.

If the documentation does not contain enough information,
say:

"I could not find enough information in the provided documentation."

Do not use your general knowledge.
Do not invent information.

DOCUMENTATION:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }
