import folium
import pandas

#throws a bunch of errors without "engine='python'"
#found solution @ https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
data = pandas.read_csv("sampling_stations.csv", engine='python')
lat = list(data["Latitude "])#, #engine='python')
lon = list(data[" Longitude"])#, #engine='python')
name = list(data["Station Name"])
status = list(data[" Status"])
#active_dates = list(data[" Active Dates"])
#active = list(data["Active    "])


map = folium.Map(location=[41.378716, -82.509539], zoom_start=16)

fgall = folium.FeatureGroup(name="sampling_stations")
fgactive = folium.FeatureGroup(name="active stations")
fginactive = folium.FeatureGroup(name="inactive stations")


for lt, ln, nm, st in zip(lat, lon, name, status):
    fgall.add_child(folium.CircleMarker(location = [lt, -(ln)],
                                    popup ="Station Name: " + str(nm),
                                    color = 'black',
                                    fill_color = 'green'))
    if st == "Active    ":
        fgactive.add_child(folium.CircleMarker(location = [lt, -(ln)],
                                    popup = "Station Name: " + str(nm),
                                    color = 'black',
                                    fill_color = 'green'))
    if st == "Inactive  ":
        fginactive.add_child(folium.CircleMarker(location = [lt, -(ln)],
                                    popup = "Station Name: " + str(nm),
                                    color = 'black',
                                    fill_color = 'red'))

#folium.Choropleth()

#map.add_child(fgall)
map.add_child(fgactive)
map.add_child(fginactive)

map.add_child(folium.LayerControl())

map.save("OWK_sampling_stations.html")
