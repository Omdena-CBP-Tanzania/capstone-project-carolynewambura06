import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor

st.title("🔮 Dar es Salaam Predictions")
st.info("These forecasts are specific to Dar es Salaam's coastal climate patterns")

@st.cache_data
def load_data():
    return pd.read_csv(r"data\tanzania_climate_data.csv")

@st.cache_resource
def load_model():
    df = load_data()
    X = df[['Month', 'Total_Rainfall_mm']]
    y = df['Average_Temperature_C']
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = load_model()

# Prediction UI
st.subheader("📈 Make a Climate Prediction")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        pred_date = st.date_input("📅 Select Forecast Date",
        min_value=datetime.today(),
        value=datetime.today() + timedelta(days=1)
 )
        

    with col2:
        rainfall = st.slider(
            "🌧️ Expected Rainfall (mm)", 
            min_value=0, 
            max_value=300, 
            value=120,
            help="Estimate based on seasonal expectations or forecasts"
        )

    submitted = st.form_submit_button("🔮 Predict Temperature")

if submitted:
    try:
        # Prepare input features
        input_data = pd.DataFrame({
            'Month': [pred_date.month],
            'Total_Rainfall_mm': [rainfall]
        })

        # Make prediction
        pred_temp = model.predict(input_data)[0]

        # Display prediction
        st.success(f"""
        ### 🌡️ Predicted Temperature: **{pred_temp:.1f}°C**
        *For {pred_date.strftime('%B %d, %Y')} in Dar es Salaam*
        """)

        # Show historical average
        df = load_data()
        historical_avg = df[df['Month'] == pred_date.month]['Average_Temperature_C'].mean()

        st.metric(
            "📊 Historical Avg. Temperature",
            f"{historical_avg:.1f}°C",
            delta=f"{pred_temp - historical_avg:+.1f}°C difference"
        )

    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
