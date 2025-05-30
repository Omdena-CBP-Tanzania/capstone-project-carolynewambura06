import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("data/tanzania_climate_data.csv")

def create_rainfall_heatmap(df):
    """Create a rainfall heatmap using matplotlib"""
    pivot = df.pivot_table(index='Year', columns='Month', values='Total_Rainfall_mm')
    
    fig, ax = plt.subplots(figsize=(12,6))
    im = ax.imshow(pivot, cmap='Blues', aspect='auto')
    
    ax.set_xticks(range(12))
    ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                       'Jul','Aug','Sep','Oct','Nov','Dec'])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    
    plt.xlabel('Month')
    plt.ylabel('Year')
    plt.title('Monthly Rainfall Heatmap')
    plt.colorbar(im, label='Rainfall (mm)')
    
    return fig

df = load_data()
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str))

st.title("📊 Historical Climate Trends")

# 1. CORRELATION MAP (NEW)
st.header("Climate Variables Correlation")
corr = df[['Average_Temperature_C', 'Total_Rainfall_mm', 'Humidity', 'Wind_Speed']].corr()
fig_corr, ax_corr = plt.subplots(figsize=(8,6))
sns.heatmap(corr, 
            annot=True, 
            cmap='coolwarm', 
            fmt=".2f",
            linewidths=0.5)
plt.title("How Variables Relate to Each Other")
st.pyplot(fig_corr)

tab1, tab2 = st.tabs(["Temperature", "Rainfall"])

with tab1:
    # 2. TEMPERATURE DISTRIBUTION (NEW)
    st.subheader("Temperature Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_hist = plt.figure()
        sns.histplot(df['Average_Temperature_C'], 
                    kde=True,
                    bins=20,
                    color='coral')
        plt.xlabel("Temperature (°C)")
        plt.title("Frequency Distribution")
        st.pyplot(fig_hist)
    
    with col2:
        fig_box = plt.figure()
        sns.boxplot(x=df['Average_Temperature_C'],
                   color='peachpuff')
        plt.xlabel("Temperature (°C)")
        plt.title("Value Spread")
        st.pyplot(fig_box)
    
    # Original temperature plot
    st.subheader("Temperature Over Time")
    fig, ax = plt.subplots(figsize=(10,4))
    ax.set_ylabel("Temperature (°C)")
    df.groupby('Date')['Average_Temperature_C'].mean().plot(ax=ax, color='orange')
    st.pyplot(fig)

with tab2:
    # Original rainfall plots
    st.subheader("Rainfall Patterns")
    fig, ax = plt.subplots(figsize=(10,4))
    ax.set_ylabel("Rainfall (mm)")
    df.groupby('Date')['Total_Rainfall_mm'].sum().plot(ax=ax)
    st.pyplot(fig)
    
    heatmap_fig = create_rainfall_heatmap(df)
    st.pyplot(heatmap_fig)