import streamlit as st
from chatbot.logic import generate_response
from chatbot.data_loader import load_data

# page config
st.set_page_config(page_title="Neo4j Chatbot", page_icon="🤖")

# title
st.title("🤖 Neo4j Chatbot (Free Version)")

# load data (only once)
if "data_loaded" not in st.session_state:
    load_data()
    st.session_state.data_loaded = True

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat (ChatGPT style)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# input box (Enter se send)
user_input = st.chat_input("Ask something...")

if user_input:
    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # bot response
    response = generate_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)