
"""
=========================================================
AI Studio - Gemini Vision
=========================================================

Author : Lakshman

Features
--------
✔ Image Understanding
✔ Image Captioning
✔ OCR (Extract Text)
✔ Custom Question Answering
✔ Streamlit Ready
=========================================================
"""

import os
from PIL import Image
from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_VISION_MODEL
)

# =====================================================
# Gemini Client
# =====================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# =====================================================
# Analyze Image
# =====================================================

def analyze_image(image_path: str, prompt: str):

    try:

        if not os.path.exists(image_path):
            return "Error: Image file not found."

        image = Image.open(image_path)

        response = client.models.generate_content(
            model=GEMINI_VISION_MODEL,
            contents=[
                prompt,
                image
            ]
        )

        return response.text

    except Exception as e:

        return f"Vision Error: {e}"


# =====================================================
# Describe Image
# =====================================================

def describe_image(image_path: str):

    prompt = """
    Describe this image in detail.

    Include:
    - Objects
    - People
    - Background
    - Colors
    - Activities
    - Overall scene
    """

    return analyze_image(image_path, prompt)


# =====================================================
# Image Caption
# =====================================================

def image_caption(image_path: str):

    prompt = """
    Generate a detailed caption for this image.
    """

    return analyze_image(image_path, prompt)


# =====================================================
# OCR
# =====================================================

def extract_text(image_path: str):

    prompt = """
    Extract all visible text from this image.
    Preserve formatting whenever possible.
    """

    return analyze_image(image_path, prompt)


# =====================================================
# Ask Question
# =====================================================

def ask_image(image_path: str, question: str):

    return analyze_image(image_path, question)


# =====================================================
# CLI Test
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🖼 AI Studio - Gemini Vision")
    print("=" * 60)

    image_path = input("Enter Image Path : ")

    if not os.path.exists(image_path):

        print("Image not found.")
        exit()

    while True:

        print("\nChoose Option")
        print("1. Describe Image")
        print("2. Caption Image")
        print("3. Extract Text (OCR)")
        print("4. Ask Question")
        print("5. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            print("\n")
            print(describe_image(image_path))

        elif choice == "2":

            print("\n")
            print(image_caption(image_path))

        elif choice == "3":

            print("\n")
            print(extract_text(image_path))

        elif choice == "4":

            question = input("\nQuestion : ")

            print("\n")
            print(ask_image(image_path, question))

        elif choice == "5":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid Choice")