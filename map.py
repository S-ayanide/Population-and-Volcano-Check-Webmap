import folium,pandas
map=folium.Map(location=[38.58, -99.09],zoom_start=5,tiles="Mapbox Bright")
points=pandas.read_csv("scripts/Volcanoes_USA.txt")

lat=list(points["LAT"])
lon=list(points["LON"])
name=list(points["NAME"])
elev=list(points["ELEV"])

def color_producer(elevation):
    if elevation<1500:
        return 'green'
    elif 1500<= elevation <2800:
        return 'orange'
    else:
        return 'red'

fgv=folium.FeatureGroup(name="Toggle Volcanoes")
for lt,ln,n,el in zip(lat,lon,name,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=n+", "+str(el)+" m",
    fill_color=color_producer(el), color='black',radius=6,fill=True,fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Toggle Population")
fgp.add_child(folium.GeoJson(data=open("scripts/world.json",'r',encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if
10000000<= x['properties']['POP2005'] <100000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
