"""
=========================================
image_generator.py
Generate Images using Hugging Face
=========================================
"""

import os
from huggingface_hub import InferenceClient
from config import HF_TOKEN, HF_IMAGE_MODEL


class ImageGenerator:

    def __init__(self):

        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HF_TOKEN
        )

        os.makedirs("generated_images", exist_ok=True)

    def generate_image(self, prompt):

        try:

            image = self.client.text_to_image(
                prompt=prompt,
                model=HF_IMAGE_MODEL
            )

            filename = (
                prompt[:20]
                .replace(" ", "_")
                .replace("/", "_")
            )

            filepath = f"generated_images/{filename}.png"

            image.save(filepath)

            return filepath

        except Exception as e:

            print(e)

            return None


generator = ImageGenerator()


def create_image(prompt):

    return generator.generate_image(prompt)


if __name__ == "__main__":

    prompt = input("Enter Prompt : ")

    path = create_image(prompt)

    if path:

        print("Image Saved :", path)

    else:

        print("Generation Failed")