import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Tanzania Climate Portal",
    page_icon="🌍",
    layout="wide"
)

# Header
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Tanzania_flag.png", width=120)
with col2:
    st.title("Tanzania Climate Analysis")
    st.caption("Historical data and predictions for Tanzania's coastal region")

# Geographic Scope Box
st.info("""
**Geographic Coverage**: This tool analyzes climate patterns specifically for **Dar es Salaam** using data from:
- Dar es Salaam International Airport (WMO Station 63894)
- Time period: 2000-2023
""")

# Key Features
st.subheader("Features")
features = """
1. **Historical Trends**: Explore 20+ years of climate data
2. **Data Analysis**: Monthly/Yearly patterns visualization
3. **Predictions**: Temperature forecasts for Dar es Salaam
"""
st.markdown(features)

# Navigation Guide
st.subheader("How to Use")
st.markdown("""
→ Use the sidebar to navigate between sections  
→ All data is specific to Dar es Salaam's coastal climate
""")

# Footer
st.divider()
st.markdown("📧 Contact: climate@darevents.go.tz | 🔗 Data Source: Tanzania Meteorological Authority")