# 🦜 Mastering LangChain: A Comprehensive Journey

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Library-green?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Welcome to the **LangChain Mastery** repository! This project is a curated collection of tutorials, experiments, and implementation patterns designed to help you navigate the powerful ecosystem of LangChain. From basic model interactions to complex RAG pipelines and autonomous agents, this repository covers it all.

---

## 📂 Project Roadmap & Structure

The repository is organized into a step-by-step modular structure, making it easy to follow the learning path from foundational concepts to advanced AI orchestration.

```
LangChain/
├── 01-LangChain/          # 🧩 Fundamentals
├── 02-models/             # 🤖 Models & Embeddings
├── 03-prompts/            # 📝 Prompts & Messaging
├── 04-Chain/              # ⛓️ Legacy Chains
├── 05-Runnable/           # ⚡ LCEL (LangChain Expression Language)
├── 06-RAG/                # 📚 Retrieval Augmented Generation
├── 07-Tools/              # 🛠️ Tools & Agents
└── 08-Projects/           # 🚀 Full-Stack Projects
```

---

### 🧩 01. LangChain Fundamentals
Introduction to the LangChain framework.
- `What_is_langchain.ipynb` — Core concepts and the problem LangChain solves.
- `Benifit_langchain.ipynb` — Why use LangChain for LLM application development.

### 🤖 02. Models & Embeddings
Deep dive into interacting with various LLM providers and embedding techniques.
- `What_is_model.ipynb` — Understanding the model interface.
- **Chat Models:**
  - `ChatBot_Openai.py`, `ChatBot_Gemini.py` — OpenAI & Google Gemini integration.
  - `Chatbot_Hugging_face.py`, `Chatbot_ollama.py` — HuggingFace & local Ollama models.
- **Embedding Models:**
  - `openai_embedding.py`, `gemini_embidding.py` — OpenAI & Gemini embeddings.
  - `huggingFace_embedding.py`, `ollama_embedding.py` — HuggingFace & Ollama embeddings.

### 📝 03. Prompts & Messaging
Mastering the art of prompt engineering and structured communication.
- `What are prompts.ipynb`, `prompt_template.ipynb` — Prompt fundamentals and templates.
- `Chat_prompt_template.ipynb` — Dynamic chat prompt construction.
- `Few_short_prompt.ipynb` — Improving model performance with few-shot examples.
- `messaging in langchain.ipynb` — Managing System, Human, and AI message types.
- `message_langchain.py` — Python implementation of message management.

### ⛓️ 04. Chains
Exploring the legacy way of chaining LLM components.
- `simple_chain.ipynb` — Single-input, single-output workflows.
- `parallel_chain.ipynb` — Executing multiple tasks simultaneously.
- `Conditional_chain.ipynb` — Logic-based branching in your application flow.

### ⚡ 05. Runnable (LCEL)
Deep dive into **LangChain Expression Language (LCEL)**, the modern standard for building chains.
- `What_are_Runnable.ipynb` — Introduction to the Runnable interface.
- `Runnable_Sequence.ipynb` — Composing components into a pipeline.
- `Runnable_Lambda.ipynb` — Wrapping custom functions for use in chains.
- `Runnable_passthrough.ipynb` — Passing data along the chain without modification.

### 📚 06. RAG (Retrieval Augmented Generation)
Complete breakdown of the RAG pipeline for building context-aware applications.

**Intro to RAG:**
- `What_is_RAG.ipynb`, `Why_use_RAG.ipynb`, `How_RAG_Work.ipynb`

**Document Loaders:**
- `What_is_Document_loader.ipynb`, `WebBaseloader.ipynb`
- **CSV:** `cvs_loader.ipynb` (with Titanic dataset)
- **PDF:** `pypdfloader_doc.ipynb`, `Directory_loader.ipynb`
- **Text:** `text_loader.ipynb` (with sample docs)

**Text Splitters:**
- `What_is_text_spliter.ipynb`, `Text_Structure.ipynb`
- `lenght_base.ipynb`, `Sementic_base.ipynb`

**Vector Stores:**
- `what_is_vectordb.ipynb`, `FAISS_DB.ipynb` (FAISS index included)

**Retrievers:**
- `What_are_retriver.ipynb`, `Vector_databese_retriver.ipynb`
- `MMR_retriver.ipynb`, `MQR_Retriver.ipynb`, `CCR_Retriver.ipynb`
- `wikipedia_retriver.ipynb`

### 🛠️ 07. Tools & Agents
Empowering LLMs to interact with the external world.
- `What_is_tool.ipynb` — Understanding the Tool interface.
- `Google_search_tool.ipynb` — Enabling web search capabilities.
- `python_repl_tool.ipynb` — Running code dynamically for calculations.
- `ReAct_Agent.py` — Implementing the Reason + Act loop for autonomous decision-making.

### 🚀 08. Projects
Real-world applications combining everything learned.

#### Multi-Type RAG
A full RAG system supporting multiple document types (PDF, text, etc.) with FAISS vector storage.
- `app.py`, `backend.py`, `backend.ipynb`, `requirements.txt`

#### Prompt Generator
A full-stack prompt engineering tool with FastAPI backend and web frontend.
```
├── api/route.py           # FastAPI routes
├── core/llm.py            # LLM configuration
├── core/prompt.py         # Prompt logic
├── frontend/              # HTML, CSS, JS UI
└── models/                # Request/Response schemas
```

#### Research Agent
An autonomous research assistant with multiple specialized tools.
```
├── main.py                # Entry point
├── api/router.py          # API endpoints
├── Core/llm.py            # LLM setup
├── Core/get_reposne.py    # Response handling
├── agent_tool/            # Tool implementations:
│   ├── web_search_tool.py    # Web search
│   ├── wiki_search_tool.py   # Wikipedia lookup
│   ├── url_reader_tool.py    # URL content reader
│   ├── calculator.py         # Math calculations
│   ├── time_tool.py          # Time/date utilities
│   └── arvic_tool.py         # Arxiv paper search
├── Frontend/              # HTML, CSS, JS UI
└── models/                # Input/Output schemas
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- An API key for your preferred LLM provider (OpenAI, Google, etc.) or Ollama installed locally.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dev-with-Mouzan/LangChian.git
   cd LangChian
   ```

2. **Install core dependencies:**
   ```bash
   pip install langchain langchain-community langchain-openai langchain-google-genai
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the relevant project directory:
   ```env
   OPENAI_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   ```

---

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** LangChain
- **Orchestration:** LCEL (LangChain Expression Language)
- **Providers:** OpenAI, Google Gemini, HuggingFace, Ollama
- **Storage:** FAISS Vector Store
- **Frontend:** HTML, CSS, JavaScript
- **API:** FastAPI

---

## 🤝 Contributing
Contributions are welcome! If you have a new LangChain pattern or a bug fix, feel free to open a Pull Request.

---

*Generated with ❤️ by Mouzan Raza*
