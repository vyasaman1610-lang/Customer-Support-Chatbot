import streamlit as st
import time
from chatbot_model import chatbot

st.set_page_config(page_title="Customer Support Bot", page_icon="💬", layout="centered")

st.title("💬 Customer Support Chatbot")
st.info("Ask anything about mental health support 💡")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:

    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Thinking stage (IMPORTANT FIX)
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = chatbot(user_input)

        # typing effect container
        placeholder = st.empty()

        typed_text = ""

        for word in response.split():
            typed_text += word + " "
            placeholder.markdown(typed_text)
            time.sleep(0.05)   # speed of typing

    # Save final response
    st.session_state.messages.append({"role": "assistant", "content": response})
