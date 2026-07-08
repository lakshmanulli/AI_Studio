
"""
==========================================================
AI Studio - Configuration
==========================================================
Author : Lakshman
Description : Central configuration file
==========================================================
"""

import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "AI Studio"
VERSION = "1.0.0"
AUTHOR = "Lakshman"

# ==========================================================
# API Keys
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

HF_TOKEN = os.getenv("HF_TOKEN")

# ==========================================================
# Gemini Models
# ==========================================================

GEMINI_CHAT_MODEL = "gemini-2.5-flash"

GEMINI_VISION_MODEL = "gemini-2.5-flash"

GEMINI_EMBEDDING_MODEL = "models/embedding-001"

# ==========================================================
# Hugging Face Model (Optional)
# ==========================================================

HF_CHAT_MODEL = "microsoft/Phi-3-mini-4k-instruct"

# ==========================================================
# RAG Settings
# ==========================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 4

# ==========================================================
# Folder Paths
# ==========================================================

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

# ==========================================================
# Create Required Folders
# ==========================================================

FOLDERS = [

    UPLOAD_FOLDER,

    PDF_FOLDER,

    IMAGE_FOLDER,

    VECTOR_DB_FOLDER,

    MODEL_FOLDER

]

for folder in FOLDERS:

    os.makedirs(
        folder,
        exist_ok=True
    )

# ==========================================================
# Validation
# ==========================================================

if not GEMINI_API_KEY:
    print("WARNING : GEMINI_API_KEY not found.")

if not HF_TOKEN:
    print("WARNING : HF_TOKEN not found (optional).")

# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print(APP_NAME)
    print("=" * 60)

    print("Version :", VERSION)

    print("\nFolders\n")

    print("Uploads :", UPLOAD_FOLDER)
    print("PDF Folder :", PDF_FOLDER)
    print("Images :", IMAGE_FOLDER)
    print("Vector DB :", VECTOR_DB_FOLDER)
    print("Models :", MODEL_FOLDER)

    print("\nConfiguration Loaded Successfully.")
