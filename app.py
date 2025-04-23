import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="GDP Statistics Dashboard", layout="wide")

# Hardcoded Credentials
USER_CREDENTIALS = {"admin": "password123", "user": "userpass"}



# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Login Page
if not st.session_state["authenticated"]:
    st.title("🔐 Login to GDP Statistics Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid username or password")
else:
    # Importing Pages
    from home import home_page
    from about import about_page
    from Dashboard import dashboard_page
    from Insights import insights_page
    from Feedback import feedback_page
    from chatbot import chatbot_page
    
    # Sidebar Navigation
    st.sidebar.title("🌐 Navigation")
    st.sidebar.info("Navigate through the GDP Statistics Dashboard to explore insights, analysis, and tools.")
    page = st.sidebar.radio("Choose a section:", 
                            ["Home", "About", "Dashboards", "Insights & Analysis", "Feedback", "Chatbot"])
    
    # Logout Button
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()
    
    # Navigation Control
    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Dashboards":
        dashboard_page()
    elif page == "Insights & Analysis":
        insights_page()
    elif page == "Feedback":
        feedback_page()
    elif page == "Chatbot":
        chatbot_page()
