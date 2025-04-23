import streamlit as st
import pandas as pd
import plotly.express as px

def dashboard_page():
    st.title("📊 Global GDP Dashboard")
    st.write("An interactive dashboard for GDP statistics, trends, and insights.")
    
    # Power BI Report URL (Replace with your actual report URL)
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=c904d630-f65f-482e-86fd-f10c784bab8d&autoAuth=true&ctid=c6809136-43da-4599-a87b-f63ebc80a21f"
    
    # Embed Power BI Report
    st.subheader("📊 Power BI Interactive Dashboard")
    st.components.v1.iframe(powerbi_url, width=1400, height=875)
    
    # Sample GDP Data
    data = {
        "Country": ["USA", "China", "Japan", "Germany", "India"],
        "GDP (Trillion $)": [26.85, 19.37, 4.30, 4.26, 3.73],
        "Growth Rate (%)": [2.3, 5.2, 1.1, 1.8, 6.7],
    }
    df = pd.DataFrame(data)
    
    # Display Key GDP Data
    st.subheader("🌍 Key GDP Statistics")
    st.dataframe(df)
    
    # GDP Bar Chart
    st.subheader("📈 GDP by Country")
    fig = px.bar(df, x="Country", y="GDP (Trillion $)", title="Top 5 GDP Economies",
                 text="GDP (Trillion $)", labels={"GDP (Trillion $)": "GDP (Trillion $)"})
    st.plotly_chart(fig)
    
    # GDP Growth Rate Pie Chart
    st.subheader("📊 GDP Growth Rate Comparison")
    fig_pie = px.pie(df, values="Growth Rate (%)", names="Country", title="GDP Growth Rate Share")
    st.plotly_chart(fig_pie)
    
if __name__ == "__main__":
    dashboard_page()
