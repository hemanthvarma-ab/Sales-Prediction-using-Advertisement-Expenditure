import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("sales_model.pkl")

st.title("📊 Sales Prediction App")
st.write("Predict product sales based on advertising expenditure.")

# User inputs
tv = st.number_input("TV Advertising Spend ($)", min_value=0.0, step=1.0)
radio = st.number_input("Radio Advertising Spend ($)", min_value=0.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Spend ($)", min_value=0.0, step=1.0)

if st.button("Predict Sales"):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)[0]
    st.success(f"✅ Predicted Sales: {prediction:.2f} units")
