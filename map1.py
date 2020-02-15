import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[48.65, -121.53], zoom_start=6) #,tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# how zips work:
# for i, j in zip([1,2,3], [4,5,6]):
#   print(i, "and", j)
#
# 1 and 4
# 2 and 5
# 3 and 6

#changed layout of variables for readability

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln],
                                popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!",
                                icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Map1.html")
