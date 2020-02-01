import plotly.graph_objects as go
from points import places
import geocoder

g = geocoder.osm('The Fat Pug')
print(g.latlng)


def drawPath(locations, geocode=True):
    names = []
    latitudes = []
    longitudes = []
    for location in locations:
        if not geocode:
            latitude, longitude = places[location]
        else:
            g = geocoder.osm(location+", Leamington Spa")
            latitude, longitude = g.latlng[0],g.latlng[1]
        names.append(location)
        latitudes.append(latitude)
        longitudes.append(longitude)

    fig = go.Figure(go.Scattermapbox(mode="text+markers+lines",
            hoverinfo='text',
            lat=latitudes,
            lon=longitudes,
            text=names,
            marker={"size": 10},))

    fig.update_layout(
        margin={"l": 0, "t": 0, "b": 0, "r": 0},
        autosize=True,
        mapbox={
            "center":{"lat":latitudes[0],"lon":longitudes[0]},
            "style": "open-street-map",
            "zoom": 14,
        },
    )

    fig.show()


drawPath(["kelseys","the fat pug", "the town house", "the old library"])