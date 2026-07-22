<div align="center">

<img src="https://img.shields.io/badge/Multi--Type-RAG-Knowledge_Engine-F59E0B?style=for-the-badge&logo=database&logoColor=white" alt="Multi Type RAG"/>

# Multi Type RAG

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-RAG-374151?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/FAISS-VectorStore-1877F2?style=flat-square" alt="FAISS"/>
  <img src="https://img.shields.io/badge/Groq-LLaMA-29B8CE?style=flat-square" alt="Groq"/>
</p>

**A powerful Retrieval-Augmented Generation system supporting multiple document types with persistent vector storage and conversational interface.**

</div>

---

## Features

- **PDF Ingestion** - Upload and index PDF documents for Q&A
- **Web Ingestion** - Pull knowledge directly from URLs
- **FAISS Vector Store** - Persistent local vector database
- **Context-Aware Responses** - Answers with source citations
- **Glassmorphism UI** - Premium neon-styled Streamlit interface
- **Session Management** - Chat history with source expanders

## Architecture

```
Multi_type_RAG/
├── app.py              # Streamlit frontend & UI
├── backend.py          # RAG pipeline & vector operations
├── Data/               # Uploaded documents
├── faiss_index/        # Persistent vector store
├── requirements.txt    # Python dependencies
└── .env               # API keys (not committed)
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Streamlit |
| AI Engine | Groq (LLaMA 3.1 8B) |
| Embeddings | Ollama (nomic-embed-text) |
| Vector Store | FAISS |
| PDF Loader | PyPDFLoader |
| Web Loader | WebBaseLoader |
| Text Splitter | RecursiveCharacterTextSplitter |

## Setup

```bash
# Clone and navigate
cd 08-Projects/Multi_type_RAG

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Ollama and pull embedding model
ollama pull nomic-embed-text

# Configure environment
echo "GROQ_API_KEY=your_key_here" > .env

# Run the application
streamlit run app.py
```

Navigate to `http://localhost:8501`

## RAG Pipeline

```
┌─────────────────────────────────────────────────────┐
│                   DATA INGESTION                    │
├─────────────────────┬───────────────────────────────┤
│      PDF Upload     │         URL Ingestion         │
│   PyPDFLoader       │      WebBaseLoader            │
└─────────┬───────────┴───────────────┬───────────────┘
          │                           │
          ▼                           ▼
┌─────────────────────────────────────────────────────┐
│            RecursiveCharacterTextSplitter            │
│              (chunk_size=500, overlap=50)            │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│          Ollama Embeddings (nomic-embed-text)        │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 FAISS Vector Store                   │
│              (Persistent Local Storage)              │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              RETRIEVAL + GENERATION                  │
│         Groq LLaMA 3.1 8B with Context              │
└─────────────────────────────────────────────────────┘
```

## API Reference

| Function | Description |
|----------|-------------|
| `ingest_pdf(path)` | Load and split PDF document |
| `ingest_url(url)` | Fetch and split web content |
| `add_to_index(docs)` | Add documents to FAISS index |
| `query_rag(query)` | Retrieve context and generate answer |
| `clear_index()` | Delete the vector store |

---

<div align="center">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge" alt="Status"/>
</div>
