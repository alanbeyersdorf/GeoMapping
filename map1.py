import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
type = list(data["TYPE"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[43.65, -113.53], zoom_start=6) #,tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="All Volcanoes")
fgstrato = folium.FeatureGroup(name="Stratovolcano")
fgfield = folium.FeatureGroup(name="Volcanic Field")
fgshield = folium.FeatureGroup(name="Shield Volcano")
fgcinder = folium.FeatureGroup(name="Cinder Cones")


# how zips work:
# for i, j in zip([1,2,3], [4,5,6]):
#   print(i, "and", j)
#
# 1 and 4
# 2 and 5
# 3 and 6

#changed layout of variables for readability

for lt, ln, el, ty in zip(lat, lon, elev, type):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                radius = 6,
                                popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!" +
                                " Type is " + str(ty),
                                fill_color=color_producer(el),
                                color = 'grey', fill_opacity=0.7))
    if ty == "Stratovolcano":
        fgstrato.add_child(folium.CircleMarker(location=[lt, ln],
                                    radius = 6,
                                    popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!" +
                                    " Type is " + str(ty),
                                    fill_color=color_producer(el),
                                    color = 'grey', fill_opacity=0.7))

    if ty == "Volcanic field":
        fgfield.add_child(folium.CircleMarker(location=[lt, ln],
                                    radius = 6,
                                    popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!" +
                                    " Type is " + str(ty),
                                    fill_color=color_producer(el),
                                    color = 'grey', fill_opacity=0.7))

    if ty == "Shield volcano":
        fgshield.add_child(folium.CircleMarker(location=[lt, ln],
                                    radius = 6,
                                    popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!" +
                                    " Type is " + str(ty),
                                    fill_color=color_producer(el),
                                    color = 'grey', fill_opacity=0.7))
    if ty == "Shield volcanoes":
        fgshield.add_child(folium.CircleMarker(location=[lt, ln],
                                    radius = 6,
                                    popup="Elevation is " + str(el) + " meters or " + str(el*3.28084) + " feet!" +
                                    " Type is " + str(ty),
                                    fill_color=color_producer(el),
                                    color = 'grey', fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
#map.add_child(fgp)
map.add_child(fgstrato)
map.add_child(fgfield)
map.add_child(fgshield)
map.add_child(folium.LayerControl())

map.save("map1.html")
