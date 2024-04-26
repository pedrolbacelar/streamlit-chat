import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#------------------------------------------
st.write("Hello World")
test_secret = st.secrets["db_username"]
st.write(test_secret)



# ------------------------------------------
st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    #--- write prompt in prompt history
    with open("database/prompt_history.txt", "a") as file:
        file.write(prompt + "\n")

    #--- Read history of prompts
    with open("database/prompt_history.txt", "r") as file:
        data = file.read()
    st.write(data)

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})