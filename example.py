import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame = True)
df = data.frame


st.title("Hello World")
st.header("Hello PEPE World")

st.dataframe(df)