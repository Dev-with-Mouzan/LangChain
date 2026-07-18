import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Suppress TensorFlow warnings and set environment variables
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress INFO and WARNING logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
os.environ['USER_AGENT'] = 'MultiTypeRAG/1.0'  # Set user agent for HTTP requests

from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Configuration
INDEX_PATH = "faiss_index"
MODEL_NAME = "llama-3.1-8b-instant"
EMBEDDING_MODEL = "nomic-embed-text:latest"

# Initialize Models
model = ChatGroq(model=MODEL_NAME,streaming=True)
embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def get_vectorstore():
    try:
        if os.path.exists(INDEX_PATH):
            return FAISS.load_local(INDEX_PATH, embedding, allow_dangerous_deserialization=True)
    except Exception as e:
        logger.error(f"Error loading vectorstore: {e}")
    return None

def save_vectorstore(vectorstore):
    vectorstore.save_local(INDEX_PATH)

def ingest_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return text_splitter.split_documents(documents)

def ingest_url(url):
    """Loads and splits content from a URL."""
    loader = WebBaseLoader(url)
    documents = loader.load()
    return text_splitter.split_documents(documents)

def add_to_index(documents):
    vectorstore = get_vectorstore()
    if vectorstore:
        vectorstore.add_documents(documents)
    else:
        vectorstore = FAISS.from_documents(documents, embedding)
    save_vectorstore(vectorstore)
    return vectorstore

def clear_index():
    """Deletes the local vectorstore index."""
    if os.path.exists(INDEX_PATH):
        import shutil
        shutil.rmtree(INDEX_PATH)
        return True
    return False

def query_rag(query):
    """Retrieves context and generates an answer using the RAG pipeline."""
    try:
        vectorstore = get_vectorstore()
        if not vectorstore:
            return "No data indexed yet. Please upload a PDF or provide a URL.", ""

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        relevant_docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        
        prompt = PromptTemplate.from_template("""Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {query}
Helpful Answer:""")
        
        chain = prompt | model
        
        response = chain.invoke({"query": query, "context": context})
        return response.content, context
    except Exception as e:
        logger.error(f"Error in query_rag: {str(e)}")
        raise e

