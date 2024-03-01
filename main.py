import streamlit as st

st.header("Weather Forecast for the Next Days")
place=st.text_input("Place:")
days=st.slider("Forecast Days", max_value=5, min_value=1)
data=st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{data} for the next {days} days in {place}")