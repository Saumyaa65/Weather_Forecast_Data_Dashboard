import streamlit as st
import plotly.express as px


def get_data(day):
    d = ["10-11-2024", "11-11-2024", "12-11-2024"]
    t = [11, 12, 15]
    t = [day * i for i in t]
    return d, t


st.header("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", max_value=5, min_value=1)
data = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{data} for the next {days} days in {place}")

dates, temperatures = get_data(days)
figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
