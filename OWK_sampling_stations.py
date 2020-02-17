import folium
import pandas

#throws a bunch of errors without "engine='python'"
#found solution @ https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
data = pandas.read_csv("sampling_stations.csv", engine='python')

map = folium.Map(location=[41.378716, -82.509539], zoom_start=16)


map.save("OWK_sampling_stations.html")
