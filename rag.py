
"""
=========================================================
AI Studio - RAG (PDF Question Answering)
=========================================================

Author : Lakshman

Features
--------
✔ Upload PDF
✔ Extract Text
✔ Split into Chunks
✔ Gemini Embeddings
✔ FAISS Vector Database
✔ Semantic Search
✔ Gemini Answer Generation
=========================================================
"""

import os
import pickle
import faiss
import numpy as np

from pypdf import PdfReader
from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_CHAT_MODEL,
    GEMINI_EMBEDDING_MODEL,
    PDF_FOLDER,
    VECTOR_DB_FOLDER,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(api_key=GEMINI_API_KEY)

# ==========================================================
# Read PDF
# ==========================================================

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text

# ==========================================================
# Split Text
# ==========================================================

def split_text(text):

    chunks = []

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunks.append(text[start:end])

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks

# ==========================================================
# Create Embedding
# ==========================================================

def get_embedding(text):

    response = client.models.embed_content(

        model=GEMINI_EMBEDDING_MODEL,

        contents=text

    )

    return np.array(
        response.embeddings[0].values,
        dtype=np.float32
    )

# ==========================================================
# Build Vector Database
# ==========================================================

def build_vector_database(pdf_path):

    text = read_pdf(pdf_path)

    chunks = split_text(text)

    embeddings = []

    for chunk in chunks:

        embeddings.append(get_embedding(chunk))

    vectors = np.vstack(embeddings)

    index = faiss.IndexFlatL2(vectors.shape[1])

    index.add(vectors)

    faiss.write_index(

        index,

        os.path.join(
            VECTOR_DB_FOLDER,
            "faiss.index"
        )

    )

    with open(

        os.path.join(
            VECTOR_DB_FOLDER,
            "chunks.pkl"
        ),

        "wb"

    ) as f:

        pickle.dump(chunks, f)

    return len(chunks)

# ==========================================================
# Search
# ==========================================================

def search(query, top_k=3):

    index = faiss.read_index(

        os.path.join(
            VECTOR_DB_FOLDER,
            "faiss.index"
        )

    )

    with open(

        os.path.join(
            VECTOR_DB_FOLDER,
            "chunks.pkl"
        ),

        "rb"

    ) as f:

        chunks = pickle.load(f)

    query_embedding = get_embedding(query)

    distances, indices = index.search(

        np.array([query_embedding]),

        top_k

    )

    context = ""

    for idx in indices[0]:

        context += chunks[idx] + "\n\n"

    return context

# ==========================================================
# Ask PDF
# ==========================================================

def ask_pdf(question):

    context = search(question)

    prompt = f"""

Answer only using the following context.

Context:

{context}

Question:

{question}

"""

    response = client.models.generate_content(

        model=GEMINI_CHAT_MODEL,

        contents=prompt

    )

    return response.text

# ==========================================================
# CLI Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)

    print("📄 AI Studio RAG")

    print("=" * 60)

    pdf_path = input("PDF Path : ")

    total = build_vector_database(pdf_path)

    print(f"\nIndexed {total} Chunks")

    while True:

        question = input("\nQuestion : ")

        if question.lower() == "exit":

            break

        answer = ask_pdf(question)

        print("\nGemini:\n")

        print(answer);