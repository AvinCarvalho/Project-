import streamlit as st

st.set_page_config(
    page_title="Registration",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
/* Hide Streamlit header, footer, toolbar, sidebar */
header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"], div[data-testid="collapsedControl"] {
    display: none !important;
}

/* Remove all padding and margins */
html, body, #root, #root > div, .main, .block-container {
    margin: 0 !important;
    padding: 0 !important;
    height: 100% !important;
}

/* Full viewport, flex center container */
[data-testid="stAppViewContainer"] {
    height: 100vh !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    background: linear-gradient(135deg, #c9d6ff 0%, #e2e2e2 100%);
}

/* Card styling */
.card {
    background: white;
    border-radius: 16px;
    padding: 40px 30px;
    max-width: 400px;
    width: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    text-align: center;
    animation: fadeIn 0.5s ease;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Title and subtitle */
h2 {
    color: #2f80ed;
    margin-bottom: 6px;
}
p {
    color: #666;
    margin-bottom: 24px;
    font-size: 14px;
}

/* Input and placeholder */
input, input::placeholder {
    font-size: 14px;
}
input {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #ccc;
    padding: 10px 12px;
    margin-bottom: 14px;
    background: #f5f8ff;
    outline: none;
}
input:focus {
    border: 1px solid #2f80ed;
    background: #ffffff;
}

/* Button */
button {
    width: 100%;
    background: #2f80ed;
    border: none;
    color: white;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
}
button:hover {
    background: #1c6dd0;
}

/* Footer text */
.signup-text {
    margin-top: 18px;
    font-size: 13px;
    color: #333;
}
.signup-text a {
    color: #2f80ed;
    font-weight: 600;
    text-decoration: none;
}
.signup-text a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<h2>Create Account</h2>', unsafe_allow_html=True)
st.markdown('<p>Quick and easy 👇</p>', unsafe_allow_html=True)

with st.form("register_form"):
    name = st.text_input("Full Name *", placeholder="Full Name *", label_visibility="collapsed")
    email = st.text_input("Email *", placeholder="Email *", label_visibility="collapsed")
    phone = st.text_input("Phone Number", placeholder="Phone Number", label_visibility="collapsed")
    password = st.text_input("Password *", type="password", placeholder="Password *", label_visibility="collapsed")
    confirm_password = st.text_input("Confirm Password *", type="password", placeholder="Confirm Password *", label_visibility="collapsed")
    submitted = st.form_submit_button("Sign Up")

if submitted:
    if not name.strip() or not email.strip() or not password.strip() or not confirm_password.strip():
        st.error("⚠️ All required fields must be filled!")
    elif password != confirm_password:
        st.error("❌ Passwords don’t match")
    else:
        st.success("✅ Registration successful!")

st.markdown("""
<div class="signup-text">
    Already have an account? <a href="#">Log in</a>
</div>
</div>
""", unsafe_allow_html=True)
