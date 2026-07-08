
"""
=========================================================
AI Studio - Gemini Chatbot
=========================================================

Author : Lakshman

Features
--------
✔ Google Gemini Chat
✔ Chat History
✔ Clear History
✔ CLI Test
=========================================================
"""

from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_CHAT_MODEL
)

# =====================================================
# Gemini Client
# =====================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# =====================================================
# Chat History
# =====================================================

chat_history = []

# =====================================================
# Gemini Chat
# =====================================================

def chat(prompt: str) -> str:
    """
    Send prompt to Gemini and return response.
    """

    try:

        response = client.models.generate_content(

            model=GEMINI_CHAT_MODEL,

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"Error : {e}"


# =====================================================
# Ask AI
# =====================================================

def ask_ai(prompt: str):

    chat_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    answer = chat(prompt)

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer


# =====================================================
# Get Chat History
# =====================================================

def get_history():

    return chat_history


# =====================================================
# Clear History
# =====================================================

def clear_history():

    chat_history.clear()


# =====================================================
# CLI Test
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 AI Studio Chatbot")
    print("=" * 60)

    while True:

        prompt = input("\nYou : ")

        if prompt.lower() in [
            "exit",
            "quit"
        ]:
            print("\nGoodbye!")
            break

        response = ask_ai(prompt)

        print("\nGemini :\n")

        print(response)

        print("-" * 60)