import os
import streamlit as st
from PIL import Image

from chatbot import ask_ai
from vision import ask_image
from image_generator import create_image

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Studio",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Create folders
# -------------------------------

os.makedirs("uploads", exist_ok=True)
os.makedirs("generated_images", exist_ok=True)

# -------------------------------
# Session State
# -------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("🤖 AI Studio")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Chatbot",
        "Vision",
        "Image Generator"
    ]
)

provider = st.sidebar.selectbox(
    "AI Provider",
    [
        "Gemini",
        "Hugging Face"
    ]
)

# =====================================================
# CHATBOT
# =====================================================

if module == "Chatbot":

    st.title("💬 AI Chatbot")

    for msg in st.session_state.chat_history:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.spinner("Thinking..."):

            response = ask_ai(
                prompt,
                provider
            )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        st.rerun()

# =====================================================
# VISION
# =====================================================

elif module == "Vision":

    st.title("🖼 Gemini Vision")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    question = st.text_input(
        "Question",
        "Describe this image."
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            use_container_width=True
        )

        image_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        image.save(image_path)

        if st.button("Analyze Image"):

            with st.spinner("Analyzing..."):

                answer = ask_image(
                    image_path,
                    question
                )

            st.success("Completed")

            st.write(answer)

# =====================================================
# IMAGE GENERATOR
# =====================================================

elif module == "Image Generator":

    st.title("🎨 AI Image Generator")

    prompt = st.text_area(
        "Enter Image Prompt"
    )

    if st.button("Generate Image"):

        with st.spinner("Generating Image..."):

            image_path = create_image(prompt)

        if image_path and os.path.exists(image_path):

            st.success("Image Generated Successfully")

            st.image(
                image_path,
                use_container_width=True
            )

            with open(image_path, "rb") as file:

                st.download_button(
                    "Download Image",
                    data=file,
                    file_name="generated_image.png",
                    mime="image/png"
                )

        else:

            st.error("Image Generation Failed")

# -------------------------------
# Footer
# -------------------------------

st.sidebar.markdown("---")
st.sidebar.info("AI Studio using Gemini + Hugging Face")