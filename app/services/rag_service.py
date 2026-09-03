from langchain_ollama import ChatOllama

from app.vectorstore.chroma_service import get_vectorstore


def get_llm():

    return ChatOllama(
        model="gemma3:4b",
        temperature=0
    )


def ask_question(question):

    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = f"""
You are a DevOps AI Assistant.

Answer the user's question using the provided documentation.

If the documentation does not contain enough information
to answer the question, say that you do not have enough
information in the provided documentation.

Do not invent information.

Documentation:
{context}

User Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content
