import os
import streamlit as st
from utils import query_agent

st.title("Let's do some analysis on your CSV")
st.header("Please upload the csv file here")

# capture the csv file
data = st.file_uploader("Upload the csv file", type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    answer = query_agent(data, query)
    st.write(answer)
