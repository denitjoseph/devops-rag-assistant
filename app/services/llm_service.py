import os

from langchain_ollama import ChatOllama


def get_llm():

    return ChatOllama(
        model="gemma3:4b",
        temperature=0,
        base_url=os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )
    )
