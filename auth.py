import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/styles.css")

# Page Title
st.markdown("# Welcome to the GDP Statistics Dashboard")
st.markdown("Please **Login** or **Sign Up** to access the dashboard.")
st.markdown("### Choose an option:")

# Login or Signup Option
auth_mode = st.radio("", ["Login", "Sign Up"])

# Function to toggle password visibility
def toggle_password_visibility():
    return st.checkbox("Show Password")

# Login Form
if auth_mode == "Login":
    st.markdown("### Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if toggle_password_visibility():
        password = st.text_input("Password", value=password)
    
    if st.button("Login"):
        # Dummy authentication check
        if username == "admin" and password == "password":
            st.success("Login successful!")
            switch_page("home")
        else:
            st.error("Invalid username or password.")
    
# Signup Form
elif auth_mode == "Sign Up":
    st.markdown("### Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if toggle_password_visibility():
        new_password = st.text_input("New Password", value=new_password)
        confirm_password = st.text_input("Confirm Password", value=confirm_password)
    
    if st.button("Sign Up"):
        if new_password == confirm_password:
            st.success("Account created successfully! Please login.")
            switch_page("auth")
        else:
            st.error("Passwords do not match.")
