"""
===========================================
AI STUDIO
Main Streamlit Application

Modules
--------
1. Chat
2. Vision
3. Image Generator
4. Video Generator
===========================================
"""

import os
import streamlit as st
from PIL import Image

from chatbot import ask_ai
from vision import ask_image
from image_generator import create_image

# Your video_generator.py should expose a generator object
# with a generate_video(prompt, filename) method.
from video_generator import VideoGenerator
from video_models.ltx_video import LTXVideo


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Studio",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------
# Create Required Folders
# ---------------------------------------

os.makedirs("uploads", exist_ok=True)
os.makedirs("generated_images", exist_ok=True)
os.makedirs("generated_videos", exist_ok=True)

# ---------------------------------------
# Session State
# ---------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------
# Video Generator
# ---------------------------------------

video_generator = VideoGenerator(
    LTXVideo()
)

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.title("🤖 AI Studio")

page = st.sidebar.radio(
    "Choose Module",
    [
        "💬 Chat",
        "🖼 Vision",
        "🎨 Image Generator",
        "🎬 Video Generator"
    ]
)

provider = st.sidebar.selectbox(
    "AI Provider",
    [
        "Gemini",
        "Hugging Face"
    ]
)

# ---------------------------------------
# CHAT
# ---------------------------------------

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

                answer = ask_ai(
                    prompt,
                    provider
                )

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# ---------------------------------------
# GEMINI VISION
# ---------------------------------------

elif page == "🖼 Vision":

    st.title("🖼 Gemini Vision")

    uploaded = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    question = st.text_input(
        "Question",
        "Describe this image."
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(
            image,
            use_container_width=True
        )

        image_path = os.path.join(
            "uploads",
            uploaded.name
        )

        image.save(image_path)

        if st.button("Analyze"):

            with st.spinner("Analyzing..."):

                result = ask_image(
                    image_path,
                    question
                )

            st.success("Completed")

            st.write(result)

# ---------------------------------------
# IMAGE GENERATOR
# ---------------------------------------

elif page == "🎨 Image Generator":

    st.title("🎨 AI Image Generator")

    prompt = st.text_area(
        "Image Prompt"
    )

    if st.button("Generate Image"):

        with st.spinner("Generating..."):

            image_path = create_image(prompt)

        if image_path:

            st.success("Image Generated")

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

            st.error("Generation Failed")

# ---------------------------------------
# VIDEO GENERATOR
# ---------------------------------------

elif page == "🎬 Video Generator":

    st.title("🎬 AI Video Generator")

    prompt = st.text_area(
        "Video Prompt"
    )

    filename = st.text_input(
        "Output Filename",
        "video.mp4"
    )

    if st.button("Generate Video"):

        with st.spinner(
            "Generating video..."
        ):

            video_path = video_generator.generate_video(
                prompt,
                filename
            )

        if os.path.exists(video_path):

            st.success(
                "Video Generated"
            )

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name=filename,
                    mime="video/mp4"
                )

        else:

            st.error(
                "Video Generation Failed"
            )