import streamlit as st

# 🎨 Apply custom CSS for style
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background: #fff9db;  /* light yellow */
        color: #333;
    }

    .login-box {
        background-color: #ffffffee;
        padding: 30px 25px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        max-width: 350px;
        margin: 100px auto;
    }

    .stButton button {
        background: #ffa502;
        color: white;
        padding: 8px 20px;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    .stButton button:hover {
        background-color: #e0a800;
    }
    </style>
""", unsafe_allow_html=True)

# 🧱 HTML wrapper for styled box
st.markdown('<div class="login-box">', unsafe_allow_html=True)

# 🔐 Title + Input fields
st.markdown("### 🔐 Dynamic Login")
st.write("Enter your username and password")

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

# ✅ Login Logic
if st.button("Login"):
    if not username or not password:
        st.warning("⚠️ Please fill in all fields!")
    elif username == "admin" and password == "1234":
        st.success(f"✅ Welcome back, {username}!")
    else:
        st.error("❌ Invalid credentials!")

# Close the styled box
st.markdown("</div>", unsafe_allow_html=True)
