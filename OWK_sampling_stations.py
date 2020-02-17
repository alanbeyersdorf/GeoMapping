import folium
import pandas

data = pandas.read_csv("sampling_stations.csv", engine='python')

map = folium.Map(location=[41.378716, -82.509539], zoom_start=16)


map.save("OWK_sampling_stations.html")
