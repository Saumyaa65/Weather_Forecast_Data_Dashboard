import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", max_value=5, min_value=1)
kind = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{kind} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        if kind== "Temperature":
            temperatures=[i["main"]["temp"]/10 for i in filtered_data]
            dates=[i["dt_txt"] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if kind=="Sky":
            condition=[i["weather"][0]["main"] for i in filtered_data]
            images={"Clear":"Images/clear.png" ,"Clouds": "Images/cloud.png",
                    "Rain":"Images/rain.png", "Snow":"Images/snow.png"}
            image_paths=[images[i] for i in condition]
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Error! Enter Correct City Name!")