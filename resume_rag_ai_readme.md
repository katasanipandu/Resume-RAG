# ResumeRAG AI

An intelligent Retrieval-Augmented Generation (RAG) application that allows users to chat with PDF documents such as resumes using LangChain, FAISS, Ollama, and Groq.

---

# Features

- Load and process PDF documents
- Split large documents into manageable chunks
- Generate embeddings using Ollama
- Store embeddings in FAISS vector database
- Retrieve relevant document chunks based on user queries
- Generate human-readable answers using LLMs
- Interactive terminal-based chatbot
- Supports local AI models using Ollama

---

# Tech Stack

- Python
- LangChain
- FAISS
- Ollama
- Groq API
- PyPDF
- Recursive Character Text Splitter
- Vector Embeddings
- RAG Architecture

---

# Project Architecture

```text
PDF Document
     ↓
Document Loader
     ↓
Text Splitter
     ↓
Embedding Model
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
LLM
     ↓
Human-Readable Response
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-link>
cd ResumeRAG-AI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Ollama Models

Install Ollama from:

https://ollama.com/

Pull the required models:

```bash
ollama pull gemma:2b
ollama pull nomic-embed-text
```

Run Ollama:

```bash
ollama run gemma:2b
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

# Project Structure

```text
ResumeRAG-AI/
│
├── rag.py
├── requirements.txt
├── .env
├── README.md
├── resume.pdf
└── venv/
```

---

# How It Works

1. Load PDF documents using PyPDFLoader
2. Split documents into chunks using RecursiveCharacterTextSplitter
3. Generate embeddings using Ollama embedding model
4. Store embeddings in FAISS vector database
5. Retrieve relevant chunks for user queries
6. Pass retrieved context to the LLM
7. Generate human-readable answers

---

# Example Questions

```text
What skills are mentioned?
What projects are included?
Tell me about internships.
What technologies does the candidate know?
What is the educational background?
```

---

# Running the Application

```bash
python rag.py
```

---

# Sample Output

```text
RAG Application Started
Type 'exit' to quit

Ask Question: What skills are mentioned?

Answer:
The resume mentions skills in Python, Flask, SQL, Machine Learning, and Data Analysis.
```

---

# What I Learned

While building this project, I learned:

- How Retrieval-Augmented Generation (RAG) works
- PDF document loading and preprocessing
- Text chunking strategies
- Vector embeddings and semantic search
- FAISS vector database integration
- Prompt engineering techniques
- Building conversational AI applications using LangChain
- Working with local LLMs using Ollama

---

# Future Improvements

- Streamlit Web UI
- Multi-PDF support
- Chat history memory
- Conversational RAG
- Source citations
- Hybrid search
- LangGraph integration
- Deployment using Docker or Cloud

---

# Author

Katasani Venkata Pandu Ranga Reddy

---

# License

This project is for educational and learning purposes.

