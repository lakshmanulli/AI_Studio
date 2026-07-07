"""
=========================================
config.py
Configuration File
=========================================
Loads API Keys from .env
"""

import os
from dotenv import load_dotenv

# --------------------------------------
# Load Environment Variables
# --------------------------------------

load_dotenv()

# --------------------------------------
# API Keys
# --------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

HF_TOKEN = os.getenv("HF_TOKEN")

# --------------------------------------
# Gemini Model
# --------------------------------------

GEMINI_MODEL = "gemini-2.5-flash"

# --------------------------------------
# Hugging Face Model
# --------------------------------------

HF_CHAT_MODEL = "microsoft/Phi-3-mini-4k-instruct"

HF_IMAGE_MODEL = "black-forest-labs/FLUX.1-schnell"

# --------------------------------------
# App Configuration
# --------------------------------------

APP_NAME = "AI Studio"

APP_VERSION = "1.0"

MAX_TOKENS = 1024

TEMPERATURE = 0.7

# --------------------------------------
# Validate Environment Variables
# --------------------------------------

if not GEMINI_API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY not found. Check your .env file."
    )

if not HF_TOKEN:
    raise ValueError(
        "❌ HF_TOKEN not found. Check your .env file."
    )