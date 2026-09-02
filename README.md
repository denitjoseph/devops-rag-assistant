# DevOps AI Assistant — RAG-Based Documentation Chatbot

An AI-powered DevOps Assistant that uses Retrieval-Augmented Generation (RAG) to answer technical DevOps questions grounded in curated documentation (Docker, Kubernetes, AWS, Jenkins, Terraform, Linux).

## 🚀 Architecture Overview

- **Frontend**: HTML5, CSS3, JavaScript (Fetch API chat interface)
- **Backend**: Python, Flask REST API (`/api/health`, `/api/chat`)
- **RAG & Vector Storage**: LangChain / Custom RAG pipeline with ChromaDB
- **LLM & Embeddings**: OpenAI API (`gpt-4o-mini` & `text-embedding-3-small`)
- **Containerization**: Docker & Docker Compose (`nginx`, `flask-api`, `chromadb`)
- **CI/CD**: Jenkins pipeline
- **Cloud Deployment**: AWS EC2 with Nginx reverse proxy

## 📁 Project Structure

```text
devops-rag-assistant/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   └── health.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── rag_service.py
│   │   ├── embedding_service.py
│   │   └── llm_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── document_loader.py
│   └── vectorstore/
│       ├── __init__.py
│       └── chroma_service.py
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .gitignore
├── requirements.txt
└── README.md
└── run.py
```

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment (`venv`)

### Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**:
   ```bash
   python run.py
   ```

4. **Access in Browser**:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to interact with the chat interface.

## 📡 API Endpoints

- **`GET /api/health`**: Health check endpoint returning `{ "status": "healthy" }`.
- **`POST /api/chat`**: Accepts `{ "question": "..." }` JSON payload and returns generated answer.
