import geocoder
g = geocoder.osm('The Fat Pug')
print(g.latlng)

# import googlemaps
# gmaps = googlemaps.Client('none')
# geocode_result1 = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# geocode_result2 = gmaps.geocode('The Fat Pug, Leamington')
# geocode_result3 = gmaps.geocode('The Fat Pug')

# print(geocode_result1)
# print(geocode_result2)
# print(geocode_result3)