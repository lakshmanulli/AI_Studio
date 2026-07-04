"""
=========================================
AI STUDIO
Main Streamlit Application
=========================================
"""

import streamlit as st
from chatbot import ask_ai

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Initialize Session State
# ----------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------------
# Sidebar
# ----------------------------------------

st.sidebar.title("🤖 AI Studio")

selected_model = st.sidebar.selectbox(
    "Choose AI Model",
    [
        "Gemini",
        "Hugging Face"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ----------------------------------------
# Main Page
# ----------------------------------------

st.title("🤖 AI Studio")

st.caption("Chat with Google Gemini or Hugging Face Models")

# ----------------------------------------
# Display Chat History
# ----------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------------
# Chat Input
# ----------------------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = ask_ai(
                    prompt,
                    selected_model
                )

            except Exception as e:

                answer = f"❌ Error: {str(e)}"

            st.markdown(answer)

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )