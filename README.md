
# 📚 RAG-Powered AI Knowledge Assistant

A **Retrieval-Augmented Generation (RAG) based AI system** that allows users to upload PDF documents and ask natural language questions.
The system retrieves relevant document chunks using **vector similarity search** and generates **context-aware answers using an LLM**.

---

💡 **One important tip:**
Add a **project screenshot later** (Swagger UI or a simple UI). Projects with images get **much more attention on GitHub**.

---

This project demonstrates a **production-style RAG architecture** used in modern GenAI applications such as **ChatGPT file upload, Perplexity AI, and enterprise document assistants**.

---

# 🚀 Features

### 📄 Document Ingestion

* Upload PDF documents
* Automatic document parsing
* Intelligent text chunking
* Vector embedding generation

### 🔍 Semantic Search

* Vector similarity search using **ChromaDB**
* Context retrieval for relevant document sections
* Fast document lookup using embeddings

### 🤖 AI Question Answering

* Ask questions in natural language
* AI answers based on retrieved document context
* Reduces hallucination using grounded responses

### ⚡ Fast API Backend

* Built with **FastAPI**
* Interactive Swagger API documentation
* Scalable backend architecture

### 🧠 Local Embedding Model

Uses **HuggingFace sentence-transformers** for reliable embeddings.

```
sentence-transformers/all-MiniLM-L6-v2
```

Advantages:

* Fast
* Free
* Works offline
* Production-ready

---

# 🏗 System Architecture

```
                 +--------------------+
                 |      User          |
                 | Ask Question       |
                 +---------+----------+
                           |
                           v
                   +-------+-------+
                   |     FastAPI   |
                   |    Backend    |
                   +-------+-------+
                           |
                           v
                   +---------------+
                   |   Retriever   |
                   |   (ChromaDB)  |
                   +---------------+
                           |
                           v
                 +-------------------+
                 |  Relevant Chunks  |
                 |   from Documents  |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 |      Gemini LLM   |
                 |   Generate Answer |
                 +-------------------+
                           |
                           v
                    AI Generated Answer
```

---

# 🛠 Tech Stack

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Python                | Core programming language  |
| FastAPI               | Backend API framework      |
| LangChain             | RAG pipeline orchestration |
| ChromaDB              | Vector database            |
| Sentence Transformers | Embedding generation       |
| Gemini API            | Large Language Model       |
| PyPDF                 | PDF document parsing       |
| Docker *(planned)*    | Deployment                 |

---

# 📂 Project Structure

```
rag-knowledge-assistant
│
├── app
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── ingest.py
│   └── config.py
│
├── data
│   └── documents
│
├── vectorstore
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/rag-knowledge-assistant.git

cd rag-knowledge-assistant
```

---

### 2️⃣ Create virtual environment

```
python3 -m venv venv
```

Activate:

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Get API key from:

```
https://aistudio.google.com
```

---

# 📥 Document Ingestion

Place PDFs inside:

```
data/documents/
```

Then run:

```
python
```

```
from app.ingest import ingest_documents

ingest_documents()
```

This will:

* Load PDF
* Split text into chunks
* Generate embeddings
* Store vectors in ChromaDB

---

# ▶ Run the API Server

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger API docs:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Ask Questions

API Endpoint:

```
POST /ask
```

Example request:

```json
{
  "question": "What is artificial intelligence?"
}
```

Example response:

```json
{
 "answer": "Artificial intelligence refers to machines that simulate human intelligence...",
 "sources": [...]
}
```

---

# 🎯 Use Cases

This system can be used for:

* Company knowledge assistants
* Research paper Q&A systems
* Legal document assistants
* Technical documentation search
* Internal company AI tools

---

# 📈 Resume Impact

Key skills demonstrated in this project:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embedding models
* LLM integration
* FastAPI backend development
* LangChain pipelines

Example resume bullet:

> Built a Retrieval-Augmented Generation (RAG) system using FastAPI, LangChain, and ChromaDB enabling semantic search and AI-powered Q&A over uploaded documents.

---

# 🚀 Future Improvements

Planned features:

* PDF upload API
* Multi-document indexing
* Streaming LLM responses
* Hybrid search (vector + keyword)
* Reranking models
* React frontend
* Docker deployment
* Authentication system

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Mohammed Nasik K**

GenAI Developer | Python | FastAPI | LangChain

GitHub:

```
https://github.com/Nasik80
```

Thank You
"""
