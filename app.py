"""
=========================================
AI STUDIO
Gemini + Hugging Face
=========================================
"""

import streamlit as st
from chatbot import ask_ai
from image_generator import create_image

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="AI Studio",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# Session State
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.title("🤖 AI Studio")

page = st.sidebar.radio(
    "Choose Module",
    [
        "💬 Chat",
        "🎨 Image Generator"
    ]
)

model = st.sidebar.selectbox(
    "AI Model",
    [
        "Gemini",
        "Hugging Face"
    ]
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------------------------
# CHAT PAGE
# ---------------------------------

if page == "💬 Chat":

    st.title("💬 AI Chatbot")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = ask_ai(prompt, model)

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# ---------------------------------
# IMAGE GENERATOR PAGE
# ---------------------------------

elif page == "🎨 Image Generator":

    st.title("🎨 AI Image Generator")

    prompt = st.text_area(
        "Describe your image",
        placeholder="Example: A futuristic AI robot working in a modern laboratory"
    )

    if st.button("Generate Image"):

        if prompt == "":
            st.warning("Please enter a prompt.")

        else:

            with st.spinner("Generating image..."):

                image_path = create_image(prompt)

            if image_path:

                st.success("Image Generated Successfully!")

                st.image(
                    image_path,
                    use_container_width=True
                )

                with open(image_path, "rb") as file:

                    st.download_button(
                        "Download Image",
                        file,
                        file_name="generated_image.png",
                        mime="image/png"
                    )

            else:

                st.error("Image generation failed.")