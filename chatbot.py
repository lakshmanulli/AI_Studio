"""
chatbot.py

Supports

1. Google Gemini
2. Hugging Face
"""

from google import genai
from huggingface_hub import InferenceClient

from config import (
    GEMINI_API_KEY,
    HF_TOKEN,
    GEMINI_MODEL,
    HF_CHAT_MODEL
)

# ----------------------------------------
# Gemini Client
# ----------------------------------------

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

# ----------------------------------------
# Hugging Face Client
# ----------------------------------------

hf_client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

# ----------------------------------------
# Gemini Chat
# ----------------------------------------

def gemini_chat(prompt):

    try:

        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ----------------------------------------
# Hugging Face Chat
# ----------------------------------------

def huggingface_chat(prompt):

    try:

        completion = hf_client.chat.completions.create(
            model=HF_CHAT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=512,
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Hugging Face Error: {e}"


# ----------------------------------------
# Main Function
# ----------------------------------------

def ask_ai(prompt, model_name="Gemini"):

    if model_name == "Gemini":
        return gemini_chat(prompt)

    elif model_name == "Hugging Face":
        return huggingface_chat(prompt)

    else:
        return "Invalid model selected."


# ----------------------------------------
# Test
# ----------------------------------------

if __name__ == "__main__":

    question = input("Ask: ")

    answer = ask_ai(question, "Gemini")

    print("\nAI Response:\n")

    print(answer)