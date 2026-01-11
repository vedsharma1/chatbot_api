import streamlit as st
from anthropic import Anthropic

client = Anthropic(api_key="")

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