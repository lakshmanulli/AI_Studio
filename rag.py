"""
=========================================
RAG.py
AI Studio - PDF Chat using Gemini + FAISS
=========================================
"""

import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_core.prompts import ChatPromptTemplate

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    EMBEDDING_MODEL,
    PDF_FOLDER,
    VECTOR_DB_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

# -----------------------------------------------------
# Google API Key
# -----------------------------------------------------

os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# -----------------------------------------------------
# Embeddings
# -----------------------------------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL
)

# -----------------------------------------------------
# Gemini Model
# -----------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    temperature=0.3
)

# -----------------------------------------------------
# Prompt
# -----------------------------------------------------

prompt = ChatPromptTemplate.from_template(
"""
You are an AI Assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say:

"I don't know based on the uploaded document."

Context:
{context}

Question:
{input}
"""
)

# -----------------------------------------------------
# Build Vector Database
# -----------------------------------------------------

def build_vector_store(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP

    )

    chunks = splitter.split_documents(documents)

    vector_db = FAISS.from_documents(

        chunks,

        embeddings

    )

    vector_db.save_local(VECTOR_DB_PATH)

    return True

# -----------------------------------------------------
# Multiple PDFs
# -----------------------------------------------------

def build_all_pdfs():

    documents = []

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                os.path.join(PDF_FOLDER, file)
            )

            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP

    )

    chunks = splitter.split_documents(documents)

    vector_db = FAISS.from_documents(

        chunks,

        embeddings

    )

    vector_db.save_local(VECTOR_DB_PATH)

    return True

# -----------------------------------------------------
# Load Vector Database
# -----------------------------------------------------

def load_vector_store():

    return FAISS.load_local(

        VECTOR_DB_PATH,

        embeddings,

        allow_dangerous_deserialization=True

    )

# -----------------------------------------------------
# Ask Question
# -----------------------------------------------------

def ask_pdf(question):

    vector_db = load_vector_store()

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 4}
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    response = retrieval_chain.invoke(
        {
            "input": question
        }
    )

    return response["answer"]

# -----------------------------------------------------
# CLI Test
# -----------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("AI Studio - RAG")
    print("=" * 50)

    pdf = input("Enter PDF Path : ")

    build_vector_store(pdf)

    print("\nVector Database Created Successfully")

    while True:

        question = input("\nAsk Question : ")

        if question.lower() == "exit":

            break

        answer = ask_pdf(question)

        print("\nAnswer:\n")

        print(answer)