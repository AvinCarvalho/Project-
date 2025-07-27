import streamlit as st

st.set_page_config(page_title="Login Page")
st.title("Welcome 👋")
st.subheader("Please log in to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
 if username == "Eesho" and password =="Eesho@123" :
  st.success = ("Login Successful")
else :
  st.error=("Login failed")
