import plotly.graph_objects as go
import geocoder
import math
import numpy as np

RESTRICTEDTO = "Leamington Spa"


class Location:
    def __init__(self, name, lat, lon):
        self.longitude = lon
        self.latitude = lat
        self.name = name

    """Returns distance to location in meters
    Returns:
        Distance -- in meters
    """

    def distanceTo(self, otherLocation):
        R = 6372800
        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = otherLocation.latitude, otherLocation.longitude

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
                math.sin(dphi / 2) ** 2
                + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        )

        return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


class MapGenerator:
    def __init__(self, locationNames):
        self.names = locationNames

    """
    Function that geocodes and returns a list of Location objects from their names
    Returns:
        [Location object]
    """

    def decodeLocations(self):
        self.locations = []
        for name in self.names:
            print(name)
            g = geocoder.osm(name + ", " + RESTRICTEDTO)
            assert len(g) == 1, "This location is not in Leamington Spa: " + str(name)
            latitude, longitude = g.latlng[0], g.latlng[1]
            self.locations.append(Location(name, latitude, longitude))
        return self.locations

    """
    Function that renders the specified locations onto the map
    """

    def renderLocations(self, locations):
        names = []
        latitudes = []
        longitudes = []

        for location in locations:
            names.append(location.name)
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)

        fig = go.Figure(
            go.Scattermapbox(
                mode="text+markers+lines",
                hoverinfo="text",
                lat=latitudes,
                lon=longitudes,
                text=names,
                marker={"size": 10},
            )
        )

        fig.update_layout(
            margin={"l": 0, "t": 0, "b": 0, "r": 0},
            autosize=True,
            mapbox={
                "center": {"lat": latitudes[0], "lon": longitudes[0]},
                "style": "open-street-map",
                "zoom": 14,
            },
        )

        fig.show()

    def adjacency_matrix_generator(self):
        adjacency_matrix = np.zeros((len(self.locations), len(self.locations)))
        for i, place_1 in enumerate(self.locations):
            for j, place_2 in enumerate(self.locations):
                if place_1.name == place_2.name:
                    adjacency_matrix[i][j] = 0
                else:
                    adjacency_matrix[i][j] = (place_1.distanceTo(place_2))
                    adjacency_matrix[j][i] = adjacency_matrix[i][j]
        return adjacency_matrix
