"""
=========================================
chatbot.py
AI Studio Chat Module

Supports:
1. Google Gemini
2. Hugging Face
=========================================
"""

from google import genai
from huggingface_hub import InferenceClient

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    HF_TOKEN,
    HF_CHAT_MODEL,
)

# =========================================
# Gemini Client
# =========================================

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

# =========================================
# Hugging Face Client
# =========================================

hf_client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

# =========================================
# Gemini Chat
# =========================================

def gemini_chat(prompt: str) -> str:
    """
    Generate a response using Gemini.
    """

    try:

        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# =========================================
# Hugging Face Chat
# =========================================

def huggingface_chat(prompt: str) -> str:
    """
    Generate a response using Hugging Face.
    """

    try:

        response = hf_client.chat.completions.create(

            model=HF_CHAT_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=1024

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Hugging Face Error: {e}"


# =========================================
# Main Chat Function
# =========================================

def ask_ai(prompt: str, provider="Gemini") -> str:
    """
    Select AI provider.

    provider:
        Gemini
        Hugging Face
    """

    provider = provider.lower()

    if provider == "gemini":

        return gemini_chat(prompt)

    elif provider == "hugging face":

        return huggingface_chat(prompt)

    else:

        return "Invalid AI Provider."


# =========================================
# Command Line Test
# =========================================

if __name__ == "__main__":

    print("=" * 50)
    print("🤖 AI Studio Chat")
    print("=" * 50)

    provider = input(
        "Choose Provider (Gemini / Hugging Face): "
    )

    while True:

        prompt = input("\nYou: ")

        if prompt.lower() in ["exit", "quit"]:

            break

        answer = ask_ai(
            prompt,
            provider
        )

        print("\nAI:\n")

        print(answer)