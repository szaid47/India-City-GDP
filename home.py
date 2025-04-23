import streamlit as st
import base64
import os

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS for the page
local_css("assets/styles.css")

# Home Page Function
def home_page():
    st.title("Welcome to India's GDP Dashboard")
    st.subheader("🌍 A Dynamic View of India's Economy")
    st.markdown("""
        <div class="home-container">
            <section class="overview-section">
                <h3>📘 Homepage Overview</h3>
                <p>The homepage serves as a gateway to India's economic insights:</p>
                <ul>
                    <li>🚀 High-level insights into key metrics.</li>
                    <li>📊 Visual trends influencing the economy.</li>
                    <li>✨ Smooth navigation to analytical tools.</li>
                </ul>
            </section>
        </div>
    """,unsafe_allow_html=True)
    
    st.markdown("""
        <div class="home-container">
            <section class="purpose-section">
                <h3>🎯 Purpose</h3>
                <p>Offering a comprehensive look at:</p>
                <ul>
                    <li>📉 Economic health indicators.</li>
                    <li>📈 GDP growth and employment statistics.</li>
                    <li>🏭 Insights into agriculture, industry, services, and tech sectors.</li>
                </ul>
                <p>This page provides a detailed view of India's evolving economy.</p>
            </section>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="home-container">
            <section class="data-sources-section">
                <h3>📂 Data Sources</h3>
                <p>Our analysis is backed by reliable sources, including:</p>
                <ul>
                    <li>📜 Government and official economic reports.</li>
                    <li>📊 Open data portals and financial institutions.</li>
                    <li>🔍 Machine learning models for predictive insights.</li>
                </ul>
            </section>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="home-container">
            <section class="features-section">
                <h3>⚡ Key Features</h3>
                <p>Explore interactive tools for in-depth analysis:</p>
                <ul>
                    <li>📈 Real-time GDP tracking and historical comparisons.</li>
                    <li>🗺️ City-wise economic performance visualization.</li>
                    <li>📊 Sectoral breakdown of economic contributions.</li>
                    <li>🔮 Predictive analytics for future economic trends.</li>
                </ul>
            </section>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="home-container">
            <section class="future-section">
                <h3>🚀 Future Enhancements</h3>
                <p>We are continuously improving our platform with:</p>
                <ul>
                    <li>📡 AI-driven economic forecasting.</li>
                    <li>📍 Geospatial mapping for localized insights.</li>
                    <li>📢 Community-driven discussions and reports.</li>
                </ul>
            </section>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()
