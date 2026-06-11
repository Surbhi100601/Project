import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("regression_model.joblib")

# App title
st.title("Package Prediction App")

# Input CGPA
cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

# Predict button
if st.button("Predict Package"):
    prediction = model.predict(np.array([[cgpa]]))

    pred_value = float(np.array(prediction).flatten()[0])

    st.success(f"Predicted Package: {pred_value:.2f} LPA")