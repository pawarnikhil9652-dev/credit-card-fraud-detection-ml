import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("Credit Card Fraud Detection")

input_data = st.text_input("Enter 29 features separated by commas")

if st.button("Predict"):
    values = list(map(float, input_data.split(",")))
    prediction = model.predict([values])
    
    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Normal Transaction")
