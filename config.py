"""
========================================================
AI Studio Configuration
========================================================
Author : Lakshman
Description :
Central configuration for the AI Studio project.
========================================================
"""

import os
from dotenv import load_dotenv

# ========================================================
# Load Environment Variables
# ========================================================

load_dotenv()

# ========================================================
# API Keys
# ========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# ========================================================
# Gemini Models
# ========================================================

GEMINI_CHAT_MODEL = "gemini-2.5-flash"
GEMINI_VISION_MODEL = "gemini-2.5-flash"
GEMINI_EMBEDDING_MODEL = "models/embedding-001"

# ========================================================
# Hugging Face Models
# ========================================================

HF_CHAT_MODEL = "microsoft/Phi-3-mini-4k-instruct"

# Change this if you want another supported image model
HF_IMAGE_MODEL = "black-forest-labs/FLUX.1-schnell"

# ========================================================
# Application Settings
# ========================================================

TEMPERATURE = 0.7
MAX_OUTPUT_TOKENS = 1024

# ========================================================
# Folder Paths
# ========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

PDF_FOLDER = os.path.join(
    UPLOAD_FOLDER,
    "pdfs"
)

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "generated_images"
)

VECTOR_DB_FOLDER = os.path.join(
    BASE_DIR,
    "vector_db"
)

MODEL_FOLDER = os.path.join(
    BASE_DIR,
    "models"
)

# ========================================================
# RAG Settings
# ========================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 4

# ========================================================
# Create Required Folders
# ========================================================

folders = [

    UPLOAD_FOLDER,

    PDF_FOLDER,

    IMAGE_FOLDER,

    VECTOR_DB_FOLDER,

    MODEL_FOLDER

]

for folder in folders:

    os.makedirs(
        folder,
        exist_ok=True
    )

# ========================================================
# Validation
# ========================================================

if not GEMINI_API_KEY:
    print(
        "WARNING: GEMINI_API_KEY is missing in .env"
    )

if not HF_TOKEN:
    print(
        "WARNING: HF_TOKEN is missing in .env"
    )

# ========================================================
# Application Information
# ========================================================

APP_NAME = "AI Studio"

VERSION = "1.0.0"

AUTHOR = "Lakshman"

DESCRIPTION = (
    "Gemini + Hugging Face AI Studio"
)

# ========================================================
# Test
# ========================================================

if __name__ == "__main__":

    print("=" * 60)
    print(APP_NAME)
    print("=" * 60)

    print("Gemini Chat Model :", GEMINI_CHAT_MODEL)
    print("Gemini Vision Model :", GEMINI_VISION_MODEL)
    print("HF Chat Model :", HF_CHAT_MODEL)
    print("HF Image Model :", HF_IMAGE_MODEL)

    print("\nFolders\n")

    print("Uploads :", UPLOAD_FOLDER)
    print("PDFs :", PDF_FOLDER)
    print("Images :", IMAGE_FOLDER)
    print("Vector DB :", VECTOR_DB_FOLDER)
    print("Models :", MODEL_FOLDER)

    print("\nConfiguration Loaded Successfully")