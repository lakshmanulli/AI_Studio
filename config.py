"""
==========================================
AI Studio Configuration
==========================================
"""

import os
from dotenv import load_dotenv

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

# ----------------------------------------
# API Keys
# ----------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# ----------------------------------------
# Gemini Configuration
# ----------------------------------------

GEMINI_MODEL = "gemini-2.5-flash"

# ----------------------------------------
# Hugging Face Chat Model
# ----------------------------------------

HF_CHAT_MODEL = "microsoft/Phi-3-mini-4k-instruct"

# ----------------------------------------
# Hugging Face Image Model
# ----------------------------------------

HF_IMAGE_MODEL = "black-forest-labs/FLUX.1-schnell"

# ----------------------------------------
# Video Configuration
# ----------------------------------------

VIDEO_PROVIDER = "LTX"

VIDEO_MODEL = "LTX-Video"

VIDEO_WIDTH = 768

VIDEO_HEIGHT = 512

VIDEO_FPS = 16

VIDEO_DURATION = 5

VIDEO_NUM_FRAMES = VIDEO_FPS * VIDEO_DURATION

VIDEO_GUIDANCE_SCALE = 7.5

VIDEO_INFERENCE_STEPS = 30

VIDEO_SEED = 42

# ----------------------------------------
# Folder Configuration
# ----------------------------------------

UPLOAD_FOLDER = "uploads"

GENERATED_IMAGES = "generated_images"

GENERATED_VIDEOS = "generated_videos"

MODEL_FOLDER = "models"

# ----------------------------------------
# Create Required Folders
# ----------------------------------------

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(GENERATED_IMAGES, exist_ok=True)

os.makedirs(GENERATED_VIDEOS, exist_ok=True)

os.makedirs(MODEL_FOLDER, exist_ok=True)

# ----------------------------------------
# Application Configuration
# ----------------------------------------

APP_NAME = "AI Studio"

APP_VERSION = "1.0"

MAX_TOKENS = 1024

TEMPERATURE = 0.7

# ----------------------------------------
# Validate API Keys
# ----------------------------------------

if not GEMINI_API_KEY:
    print("⚠ GEMINI_API_KEY not found. Gemini features will not work.")

if not HF_TOKEN:
    print("⚠ HF_TOKEN not found. Hugging Face features will not work.")