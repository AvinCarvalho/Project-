import streamlit as st


st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")


st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding-top: 80px;
    }
    .stTextInput > div > div {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 5px;
    }
    .login-box {
        background-color: white;
        padding: 40px 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        width: 100%;
        max-width: 400px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)



st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.title("🔐 Login")
st.write("Welcome back, please enter your credentials.")

username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("✅ Login successful!")
    else:
        st.error("❌ Invalid credentials")

st.markdown('</div>', unsafe_allow_html=True)
