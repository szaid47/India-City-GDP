import streamlit as st
from streamlit_chat import message

import os
import base64

def set_bg(image_path="assets/background.jpg"):
    """Sets a background image in a Streamlit app from a local file."""
    if not os.path.exists(image_path):
        st.error(f"Error: Background image '{image_path}' not found.")
        return

    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    bg_css = f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{encoded_string}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Apply the background
set_bg()

def chatbot_page():
    st.title("🤖 Chatbot Assistant")
    st.write("Welcome to the chatbot assistant! Ask questions about the GDP Statistics Dashboard, features, or insights.")
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Input for user message
    user_input = st.text_input("You:")
    
    # If user sends a message
    if st.button("Send"):
        if user_input:
            # Store user message
            st.session_state.messages.append({"role": "user", "text": user_input})
            
            # Define responses for specific questions
            if "what is gdp" in user_input.lower():
                bot_response = (
                    "GDP, or Gross Domestic Product, is the total value of goods and services produced within a country over a specific period. "
                    "It is a key indicator of a country's economic performance."
                )
            
            elif "what does home page do" in user_input.lower():
                bot_response = (
                    "The Home page provides an overview of India's economic health with high-level insights into key metrics, "
                    "a snapshot of trends driving the economy, and easy navigation to detailed analyses."
                )
            
            elif "what does about page do" in user_input.lower():
                bot_response = (
                    "The About page explains the purpose and scope of the GDP Statistics Dashboard, giving users an understanding "
                    "of the features and insights they can explore."
                )
            
            elif "what does dashboards page do" in user_input.lower():
                bot_response = (
                    "The Dashboards page presents detailed visualizations and statistics about India's GDP, including growth trends, "
                    "sector-wise contributions, and other economic indicators."
                )
            
            elif "what does insights & analysis page do" in user_input.lower():
                bot_response = (
                    "The Insights & Analysis page offers in-depth analysis and expert interpretations of GDP data, helping users understand "
                    "economic patterns and their implications."
                )
            
            elif "what does feedback page do" in user_input.lower():
                bot_response = (
                    "The Feedback page allows users to provide their opinions, suggestions, or report issues regarding the GDP Dashboard, "
                    "helping improve the user experience."
                )
            
            elif "what does chatbot page do" in user_input.lower():
                bot_response = (
                    "The Chatbot page is designed to assist users with their queries about the GDP Dashboard, including navigating through "
                    "the platform and understanding different features."
                )
            
            else:
                bot_response = "I am here to help with your questions about the GDP Dashboard."
            
            # Store bot response
            st.session_state.messages.append({"role": "bot", "text": bot_response})
    
    # Display chat history
    for msg in st.session_state.messages:
        message(msg["text"], is_user=(msg["role"] == "user"))
