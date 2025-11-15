import streamlit as st
from datetime import date
import base64
import requests

col1, col2 = st.columns([1, 4])   # Adjust width ratio as needed

with col1:
    st.image("images/weather.png", width=120)

with col2:
    st.markdown(
        "<h1 style='padding-top: 15px;'>Weather Prediction App</h1>",
        unsafe_allow_html=True
    )

selected_date = st.date_input("yyyy-mm-dd", value=date.today())

max_temp = st.text_input("Enter a max temp that can be reached in °C", placeholder=30)
min_temp = st.text_input("Enter a min temp that can be reached in °C", placeholder=20)
precipitation = st.text_input("Enter Precipiation value", placeholder= 0.7)
wind = st.text_input("Enter wind speed", placeholder=4.0)

if st.button("Submit"):
    if not max_temp or not min_temp or not precipitation or not wind:
        st.warning("Enter all the fields")
    elif float(min_temp) >= float(max_temp):
        st.error("Min temp cannot be greater than max temp")
    else:
        payload = {
            "prediction_date": selected_date.strftime("%Y-%m-%d"),
            "min_temp": min_temp,
            "max_temp": max_temp,
            "precipitation": precipitation,
            "wind": wind
        }
        try:
            res = requests.post("http://127.0.0.1:8000/predict", json=payload)

            if res.status_code == 200:
                result = res.json()
                st.success(f"Prediction: {result['Prediction']}")
            else:
                st.error(f"Error: {res.status_code}")
                st.write(res.text)
    
        except Exception as e:
            st.error("Could not connect to API")
            st.write(e)