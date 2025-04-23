import streamlit as st
import pandas as pd
from datetime import datetime
import os

def feedback_page():
    st.title("📝 Feedback")
    st.write("We value your feedback to improve the GDP Statistics Dashboard. "
             "Please let us know your thoughts, suggestions, or any issues you've encountered.")
    
    # User Inputs
    name = st.text_input("Your Name", placeholder="Enter your name here")
    email = st.text_input("Your Email (optional)", placeholder="Enter your email for follow-up (optional)")
    category = st.selectbox(
        "Feedback Category",
        ["General Feedback", "Bug Report", "Feature Request", "Other"],
        help="What is your feedback related to?"
    )
    feedback = st.text_area("Your Feedback", placeholder="Write your feedback here...")
    satisfaction = st.slider(
        "How satisfied are you with the dashboard?",
        min_value=1,
        max_value=5,
        value=3,
        format="%d 🌟"
    )
    
    # Submit Button
    if st.button("Submit Feedback"):
        if feedback:
            # Create a DataFrame to store feedback
            feedback_data = {
                "Name": name,
                "Email": email,
                "Category": category,
                "Feedback": feedback,
                "Satisfaction": satisfaction,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            folder_path = "feedback"
            file_path = os.path.join(folder_path, "feedback.csv")
            # Convert to DataFrame and save to CSV
            df = pd.DataFrame([feedback_data])
            df.to_csv(file_path, mode='a', header=False, index=False)
            
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter your feedback before submitting.")
    
if __name__ == "__main__":
    feedback_page()
