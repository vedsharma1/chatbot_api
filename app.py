import streamlit as st
from anthropic import Anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

st.title("Simple Chatbot 😊")

user_input = st.text_input("Say something:")

if st.button("Send") and user_input:
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        messages=[
            {"role": "user", "content": user_input}
        ],
        max_tokens=300
    )


    st.write("Bot:", response.content[0].text)

