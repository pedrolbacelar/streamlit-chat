import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#------------------------------------------
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.Name} has a :{row.Pet}:")
st.write("Hey :dog:")


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

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})