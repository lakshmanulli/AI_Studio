"""
===========================================
vision.py
Gemini Vision using google-genai SDK
===========================================
"""

from google import genai
from PIL import Image

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

# ------------------------------------
# Gemini Client
# ------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ------------------------------------
# Image Analyzer
# ------------------------------------

def analyze_image(image_path, prompt):

    try:

        image = Image.open(image_path)

        response = client.models.generate_content(

            model=GEMINI_MODEL,

            contents=[
                prompt,
                image
            ]

        )

        return response.text

    except Exception as e:

        return f"Error : {e}"


# ------------------------------------
# Image Caption
# ------------------------------------

def image_caption(image_path):

    prompt = "Describe this image in detail."

    return analyze_image(image_path, prompt)


# ------------------------------------
# OCR
# ------------------------------------

def extract_text(image_path):

    prompt = """
Extract all visible text from the image.
Keep formatting whenever possible.
"""

    return analyze_image(image_path, prompt)


# ------------------------------------
# Object Detection
# ------------------------------------

def detect_objects(image_path):

    prompt = """
Identify every object visible in this image.
"""

    return analyze_image(image_path, prompt)


# ------------------------------------
# Scene Description
# ------------------------------------

def scene_description(image_path):

    prompt = """
Explain the complete scene in detail.
"""

    return analyze_image(image_path, prompt)


# ------------------------------------
# Custom Question
# ------------------------------------

def ask_image(image_path, question):

    return analyze_image(image_path, question)


# ------------------------------------
# Testing
# ------------------------------------

if __name__ == "__main__":

    path = input("Image Path : ")

    question = input("Ask : ")

    answer = ask_image(path, question)

    print("\n")

    print(answer)