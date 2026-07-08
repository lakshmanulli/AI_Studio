
"""
=========================================================
AI Studio - AI Image Generator
=========================================================

Author : Lakshman

Features
--------
✔ Free Image Generation
✔ No API Key Required
✔ Saves Images
✔ Streamlit Ready
✔ Error Handling
=========================================================
"""

import os
from io import BytesIO
from datetime import datetime

import requests
from PIL import Image

from config import IMAGE_FOLDER

# ==========================================================
# Create Image Folder
# ==========================================================

os.makedirs(
    IMAGE_FOLDER,
    exist_ok=True
)

# ==========================================================
# Generate Image
# ==========================================================

def generate_image(prompt: str):

    try:

        prompt = prompt.replace(" ", "%20")

        url = (
            f"https://image.pollinations.ai/prompt/{prompt}"
        )

        response = requests.get(
            url,
            timeout=120
        )

        response.raise_for_status()

        image = Image.open(
            BytesIO(response.content)
        )

        filename = (
            datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".png"
        )

        output_path = os.path.join(
            IMAGE_FOLDER,
            filename
        )

        image.save(output_path)

        return output_path

    except Exception as e:

        return f"Image Generation Error : {e}"


# ==========================================================
# Display Image
# ==========================================================

def show_image(image_path):

    image = Image.open(image_path)

    image.show()


# ==========================================================
# CLI Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🎨 AI Studio Image Generator")
    print("=" * 60)

    while True:

        prompt = input(
            "\nEnter Prompt (exit to quit): "
        )

        if prompt.lower() == "exit":

            break

        result = generate_image(prompt)

        if os.path.exists(result):

            print("\nImage Generated Successfully")

            print(result)

            show_image(result)

        else:

            print("\n" + result)