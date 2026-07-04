import streamlit as st

from chatbot import ask_ai

st.title("🤖 AI Studio")

model = st.sidebar.selectbox(

    "Choose Model",

    [

        "Gemini",

        "Hugging Face"

    ]

)

question = st.text_input("Ask anything")

if st.button("Send"):

    answer = ask_ai(question, model)

    st.write(answer)