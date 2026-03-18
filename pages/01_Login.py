import streamlit as st
from utils import authenticate_user, sign_up_user

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

st.title("🔐 Login")
st.markdown("---")

# Check if already logged in
if st.session_state.get("authenticated"):
    st.success("You are already logged in!")
    st.switch_page("pages/02_Add_Users.py")

# Login/Sign Up toggle
tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    st.subheader("Login to your account")
    
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Login", use_container_width=True)
        
        if submit_button:
            if not email or not password:
                st.error("Please enter both email and password")
            else:
                with st.spinner("Authenticating..."):
                    result = authenticate_user(email, password)
                    if result["success"]:
                        st.session_state.authenticated = True
                        st.session_state.user = email
                        st.success("Login successful! 🎉")
                        st.switch_page("pages/02_Add_Users.py")
                    else:
                        st.error(f"Login failed: {result['error']}")

with tab2:
    st.subheader("Create a new account")
    
    with st.form("signup_form"):
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        signup_submit = st.form_submit_button("Sign Up", use_container_width=True)
        
        if signup_submit:
            if not signup_email or not signup_password or not confirm_password:
                st.error("Please fill in all fields")
            elif signup_password != confirm_password:
                st.error("Passwords do not match")
            elif len(signup_password) < 6:
                st.error("Password must be at least 6 characters long")
            else:
                with st.spinner("Creating account..."):
                    result = sign_up_user(signup_email, signup_password)
                    if result["success"]:
                        st.success("Account created successfully! Please login now.")
                    else:
                        st.error(f"Sign up failed: {result['error']}")
