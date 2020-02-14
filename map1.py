import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[41.65, -83.53], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# how zips work:
# for i, j in zip([1,2,3], [4,5,6]):
#   print(i, "and", j)
#
# 1 and 4
# 2 and 5
# 3 and 6

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
