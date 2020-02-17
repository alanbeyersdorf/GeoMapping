import folium
import pandas

#throws a bunch of errors without "engine='python'"
#found solution @ https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
data = pandas.read_csv("sampling_stations.csv", engine='python')
lat = list(data["Latitude "])#, #engine='python')
lon = list(data[" Longitude"])#, #engine='python')
name = list(data["Station Name"])


map = folium.Map(location=[41.378716, -82.509539], zoom_start=16)

fg = folium.FeatureGroup(name="sampling_stations")


for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.CircleMarker(location = [lt, -(ln)],
                                    popup ="Station Name: " + str(nm),
                                    color = 'black',
                                    fill_color = 'green'))

map.add_child(fg)

map.add_child(folium.LayerControl())

map.save("OWK_sampling_stations.html")
