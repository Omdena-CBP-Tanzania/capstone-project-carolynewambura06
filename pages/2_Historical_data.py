import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("data/tanzania_climate_data.csv")

def create_rainfall_heatmap(df):
    """Create a rainfall heatmap using matplotlib"""
    pivot = df.pivot_table(index='Year', columns='Month', values='Total_Rainfall_mm')
    
    fig, ax = plt.subplots(figsize=(12,6))
    im = ax.imshow(pivot, cmap='Blues', aspect='auto')
    
    # Set ticks and labels
    ax.set_xticks(range(12))
    ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                       'Jul','Aug','Sep','Oct','Nov','Dec'])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    
    # Add labels and colorbar
    plt.xlabel('Month')
    plt.ylabel('Year')
    plt.title('Monthly Rainfall Heatmap')
    plt.colorbar(im, label='Rainfall (mm)')
    
    return fig

df = load_data()
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str))

st.title("📊 Historical Climate Trends")

tab1, tab2 = st.tabs(["Temperature", "Rainfall"])

with tab1:
    st.subheader("Temperature Patterns")
    fig, ax = plt.subplots(figsize=(10,4))
    df.groupby('Date')['Average_Temperature_C'].mean().plot(ax=ax, color='orange')
    st.pyplot(fig)

with tab2:
    st.subheader("Rainfall Patterns")
    fig, ax = plt.subplots(figsize=(10,4))
    df.groupby('Date')['Total_Rainfall_mm'].sum().plot(ax=ax)
    st.pyplot(fig)
    
    # Use st.pyplot() for matplotlib figures, not st.altair_chart()
    heatmap_fig = create_rainfall_heatmap(df)
    st.pyplot(heatmap_fig)