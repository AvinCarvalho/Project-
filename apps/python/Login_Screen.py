import streamlit as st

# Apply some custom CSS for styling
st.markdown(
    """
    <style>
    .login-container {
        background-color: #e0e0e0;
        border-radius: 20px;
        padding: 40px;
        max-width: 600px;
        margin: auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #555555;
        margin-bottom: 30px;
    }
    label {
        font-weight: 600;
        color: #666666;
    }
    .forgot-password {
        font-size: 0.9rem;
        color: #999999;
        float: right;
        cursor: pointer;
    }
    .login-btn {
        background-color: #b06ca3;
        color: white;
        padding: 12px 0;
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
        cursor: pointer;
    }
    .or-continue {
        text-align: center;
        color: #777777;
        margin: 25px 0 15px 0;
        font-size: 0.9rem;
    }
    .social-buttons button {
        background: white;
        border-radius: 20px;
        padding: 8px 0;
        font-size: 1.1rem;
        margin: 0 5px;
        border: 1px solid #999999;
        cursor: pointer;
    }
    .signup-text {
        text-align: center;
        font-size: 0.85rem;
        color: #666666;
        margin-top: 20px;
    }
    .signup-text a {
        color: #b06ca3;
        text-decoration: none;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Container for the login form
with st.container():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown('<p><strong>Logo Here</strong></p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Welcome back !!</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="title">Log In</h1>', unsafe_allow_html=True)

    email = st.text_input("Email/User Name", placeholder="login@gmail.com")
    col1, col2 = st.columns([7,3])
    with col1:
        password = st.text_input("Password", type="password", placeholder="************")
    with col2:
        st.markdown('<p class="forgot-password">Forgot Password?</p>', unsafe_allow_html=True)

    login_btn = st.button("LOGIN →", key="login", help="Click to login")

    # st.markdown('<p class="or-continue">or continue with</p>', unsafe_allow_html=True)

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     if st.button("Google"):
    #         st.write("Google login clicked")
    # with col2:
    #     if st.button("GitHub"):
    #         st.write("GitHub login clicked")
    # with col3:
    #     if st.button("Facebook"):
    #         st.write("Facebook login clicked")

    st.markdown(
        '<p class="signup-text">Don\'t have an account yet? <a href="#">Sign up</a></p>',
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
