import streamlit as st
from joblib import load
import numpy as np

# Load the trained model
model = load('housing_model.joblib')

# App title
st.title("California Housing Price Prediction")
st.markdown("Enter the details of the house to predict its median price.")

# User inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Median Age of House", value=29)
total_rooms = st.number_input("Total Rooms", value=880)
total_bedrooms = st.number_input("Total Bedrooms", value=129)
population = st.number_input("Population", value=322)
households = st.number_input("Households", value=126)
median_income = st.number_input("Median Income", value=8.3)

# Predict button
if st.button("Predict House Price"):
    input_data = np.array([[longitude, latitude, housing_median_age, total_rooms,
                            total_bedrooms, population, households, median_income]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Median House Price: ${prediction[0]:,.2f}")
