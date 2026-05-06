import os
from dotenv import load_dotenv

load_dotenv()

# PDF Loader
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("KVPANDURANGAREDDY-228R1A6789.pdf")
content = loader.load()

# Text Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

final_docs = text_splitter.split_documents(content)

# Embeddings
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="gemma:2b"
)

# Vector Store
from langchain_community.vectorstores import FAISS

db = FAISS.from_documents(final_docs, embeddings)

# Retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# -----------------------------
# LLM
# -----------------------------
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model="gemma:2b")

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an intelligent assistant.

Answer the question based only on the provided context.

Context:
{context}

Question:
{question}

Provide a clear, concise, and human-readable answer.
""")

# -----------------------------
# Output Parser
# -----------------------------
output_parser = StrOutputParser()

# -----------------------------
# Chat Loop
# -----------------------------
print("\nRAG Application Started")
print("Type 'exit' to quit\n")

while True:

    query = input("Ask Question: ")

    if query.lower() == "exit":
        break

    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)

    # Combine context
    context = "\n\n".join([
        doc.page_content for doc in retrieved_docs
    ])

    # Create chain
    chain = prompt | llm | output_parser

    # Generate final response
    response = chain.invoke({
        "context": context,
        "question": query
    })

    print("\nAnswer:\n")
    print(response)

    print("\n" + "-"*50 + "\n")