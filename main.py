import streamlit as sp
from backendd import get_data
# import matplotlib as mp
import plotly.express as px

sp.title("Weather Forecast For The Next Days")
place = sp.text_input("place : ")
days = sp.slider("forecast days", min_value=1, max_value=5, help="select the no of days")
option = sp.selectbox("select data to view",
                      ("Temperature", "sky"))
sp.subheader(f"{option} for the next {days} days in {place}")


# def get_data(days):
#     dates = ["2023-21-11","2023-22-11","2023-22-11","2023-23-11","2023-24-11"]
#     temp = [10,11,12,13,14,15]
#     temp = [days * i for i in temp]
#     return dates,temp
if place:
    try:

        filter_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
            # d,t = get_data(days)
            figure = px.line(x=dates,y=temperatures,labels={"x":"Date", "y":"temperature (c)"})
            sp.plotly_chart(figure)
        elif option == "sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            img_paths = [images[condition] for condition in sky_conditions]
            sp.image(img_paths, width=115)
    except KeyError:
        sp.write("place not exist")
