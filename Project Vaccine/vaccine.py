import folium
import pandas as pd

data= pd.read_csv("state")
lat = list(data["Lat"])
lon = list(data["Long"])
st = list(data["State"])
vac = list(data["Number of Vaccines"])

html = """<h4>Vaccine information:</h4>         # Basic HTML code for the heading 
State and Number: %s   ,  
"""
def color_producer(number):
    if number < 1000:
        return "green"
    elif 1000 <= number <=10000 :
        return "orange"
    else :
        return "red"

map = folium.Map(location= [22.55  , 79.65], zoom_start =5, titles = "Stamen Terrain")

fg = folium.FeatureGroup(name= "My Map")

for lt,ln,st,vac in zip(lat, lon, st , vac) :
     iframe = folium.IFrame(html=html % str(st)+ str(vac), width=200, height=100)
     fg.add_child(folium.Marker(location= [lt , ln], popup =folium.Popup(iframe), icon=folium.Icon(color=color_producer(vac))))

map.add_child(fg)
map.save("Map1.html")