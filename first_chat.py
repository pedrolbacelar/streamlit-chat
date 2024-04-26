import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#------------------------------------------
st.write("Hello World")
test_secret = st.secrets["db_username"]
st.write(test_secret)



