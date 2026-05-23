# 🦜 Mastering LangChain: A Comprehensive Journey

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Library-green?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Welcome to the **LangChain Mastery** repository! This project is a curated collection of tutorials, experiments, and implementation patterns designed to help you navigate the powerful ecosystem of LangChain. From basic model interactions to complex RAG pipelines and autonomous agents, this repository covers it all.

---

## 📂 Project Roadmap & Structure

The repository is organized into a step-by-step modular structure, making it easy to follow the learning path from foundational concepts to advanced AI orchestration.

### 🧩 01. LangChain Fundamentals
Introduction to the LangChain framework.
- `What_is_langchain.ipynb`: Core concepts and the problem LangChain solves.
- `Benifit_langchain.ipynb`: Why use LangChain for LLM application development.

### 🤖 02. Models & Embeddings
Deep dive into interacting with various LLM providers and embedding techniques.
- **Chat Models**: Implementation examples for **OpenAI**, **Google Gemini**, **HuggingFace**, and **Ollama**.
- **Embedding Models**: How to convert text into vector representations using different providers.
- `What_is_model.ipynb`: Understanding the model interface.

### 📝 03. Prompts & Messaging
Mastering the art of prompt engineering and structured communication.
- `prompt_template.ipynb`: Dynamic prompt generation.
- `Few_short_prompt.ipynb`: Improving model performance with examples.
- `message_langchain.py`: Managing different message types (System, Human, AI).
- `Combination(Message,Prompts).py`: Blending prompts and complex message structures.

### ⛓️ 05. Chains
Exploring the legacy and modern ways of chaining LLM components.
- `simple_chain.ipynb`: Single-input, single-output workflows.
- `parallel_chain.ipynb`: Executing multiple tasks simultaneously.
- `Conditional_chain.ipynb`: Logic-based branching in your application flow.

### ⚡ 06. Runnable (LCEL)
Deep dive into **LangChain Expression Language (LCEL)**, the modern standard for building chains.
- `What_are_Runnable.ipynb`: Introduction to the Runnable interface.
- `Runnable_Sequence.ipynb`: Composing components into a pipeline.
- `Runnable_Lambda.ipynb`: Wrapping custom functions for use in chains.
- `Runnable_passthrough.ipynb`: Passing data along the chain without modification.

### 📚 07. RAG (Retrieval Augmented Generation)
Complete breakdown of the RAG pipeline for building context-aware applications.
- **Document Loader**: Importing data from various sources.
- **Text Splitter**: Chunking large datasets for vector storage.
- **Vector Store**: Storing and managing high-dimensional embeddings.
- **Retriever**: Efficiently fetching relevant context for queries.

### 🛠️ 08. Tools & Agents
Empowering LLMs to interact with the external world.
- `What_is_tool.ipynb`: Understanding the Tool interface.
- `Google_search_tool.ipynb`: Enabling web search capabilities.
- `python_repl_tool.ipynb`: Running code dynamically for calculations.
- `ReAct_Agent.py`: Implementing the Reason + Act loop for autonomous decision-making.

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
   Create a `.env` file in the root directory:
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
- **Storage:** Vector Stores (ChromaDB/FAISS)

---

## 🤝 Contributing
Contributions are welcome! If you have a new LangChain pattern or a bug fix, feel free to open a Pull Request.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
*Generated with ❤️ by Mouzan Raza*
# LangChain
