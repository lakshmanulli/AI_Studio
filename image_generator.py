"""
=========================================
AI Studio
Image Generator using Hugging Face
=========================================
"""

import os
from huggingface_hub import InferenceClient

from config import (
    HF_TOKEN,
    HF_IMAGE_MODEL,
    IMAGE_FOLDER
)

# --------------------------------------
# Create output folder
# --------------------------------------

os.makedirs(
    IMAGE_FOLDER,
    exist_ok=True
)

# --------------------------------------
# Hugging Face Client
# --------------------------------------

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

# --------------------------------------
# Image Generator
# --------------------------------------

def create_image(
    prompt: str,
    filename: str = "generated_image.png"
):

    try:

        image = client.text_to_image(

            prompt=prompt,

            model=HF_IMAGE_MODEL

        )

        output_path = os.path.join(
            IMAGE_FOLDER,
            filename
        )

        image.save(output_path)

        return output_path

    except Exception as e:

        print(f"Image Generation Error : {e}")

        return None


# --------------------------------------
# CLI Test
# --------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("AI Studio Image Generator")
    print("=" * 50)

    prompt = input("\nEnter Prompt : ")

    image_path = create_image(prompt)

    if image_path:

        print("\nImage Saved Successfully")

        print(image_path)

    else:

        print("\nGeneration Failed")