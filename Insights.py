import streamlit as st
import pandas as pd


def insights_page():
    st.title("📊 GDP Insights")
    st.subheader("Economic Overview")
    st.write("Explore the latest economic statistics and trends through detailed visualizations and summary cards.")
    
    st.markdown("---")
    
    st.subheader("Key Economic Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### GDP Growth Rate")
        st.markdown("## 3.8%")
        st.markdown("<span style='color: green;'>▲ 0.5%</span>", unsafe_allow_html=True)
        st.caption("Quarter-over-quarter growth.")
    
    with col2:
        st.markdown("### Employment Rate")
        st.markdown("## 95.2%")
        st.markdown("<span style='color: green;'>▲ 0.3%</span>", unsafe_allow_html=True)
        st.caption("Percentage of the workforce employed.")
    
    with col3:
        st.markdown("### Inflation Rate")
        st.markdown("## 4.1%")
        st.markdown("<span style='color: green;'>▲ 0.2%</span>", unsafe_allow_html=True)
        st.caption("Year-over-year price change.")
    
    st.markdown("---")
    
    st.subheader("Sector Performance")
    st.write("Analyze the contributions of various sectors to the GDP. The performance indicators highlight the economic health of major industries.")
    
    # Sample Data for Sector Performance
    data = {
        "Sector": ["Agriculture", "Manufacturing", "Services", "Construction", "Retail"],
        "Contribution to GDP (%)": [12.3, 24.7, 53.2, 6.4, 3.4],
        "Growth Rate (%)": [2.1, 3.4, 4.0, 1.8, 2.5]
    }
    
    df = pd.DataFrame(data)
    st.table(df)

if __name__ == "__main__":
    insights_page()
