"""
====================================================
AI Studio Chatbot
====================================================

Supports:
1. Google Gemini
2. Hugging Face

Author : Lakshman
====================================================
"""

from google import genai
from huggingface_hub import InferenceClient

from config import (
    GEMINI_API_KEY,
    GEMINI_CHAT_MODEL,
    HF_TOKEN,
    HF_CHAT_MODEL
)

# =====================================================
# Gemini Client
# =====================================================

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

# =====================================================
# Hugging Face Client
# =====================================================

hf_client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

# =====================================================
# Chat History
# =====================================================

chat_history = []


# =====================================================
# Gemini Chat
# =====================================================

def gemini_chat(prompt: str) -> str:
    """
    Chat using Gemini
    """

    try:

        response = gemini_client.models.generate_content(
            model=GEMINI_CHAT_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error : {e}"


# =====================================================
# Hugging Face Chat
# =====================================================

def huggingface_chat(prompt: str) -> str:
    """
    Chat using Hugging Face
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

        return f"Hugging Face Error : {e}"


# =====================================================
# Main Chat Function
# =====================================================

def ask_ai(
    prompt: str,
    provider: str = "Gemini"
) -> str:
    """
    Main chat function
    """

    provider = provider.lower()

    chat_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    if provider == "gemini":

        answer = gemini_chat(prompt)

    elif provider in ["hugging face", "huggingface"]:

        answer = huggingface_chat(prompt)

    else:

        answer = "Invalid AI Provider"

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer


# =====================================================
# Chat History
# =====================================================

def get_chat_history():
    return chat_history


def clear_chat():
    chat_history.clear()


# =====================================================
# CLI Test
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 AI Studio Chatbot")
    print("=" * 60)

    provider = input(
        "\nChoose Provider (Gemini/Hugging Face): "
    )

    while True:

        prompt = input("\nYou : ")

        if prompt.lower() in [
            "exit",
            "quit"
        ]:
            print("Goodbye!")
            break

        response = ask_ai(
            prompt,
            provider
        )

        print("\nAI:\n")

        print(response)

        print("-" * 60)