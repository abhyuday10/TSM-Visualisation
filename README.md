# TSM-Visualisation
Visualising the TSM problem in the context of local pubs.

# Installing dependencies
```
git clone https://github.com/abhyuday10/TSM-Visualisation
pip install -r requirements.txt
```

# Usage Details

Create a list of locations
```python
NamesOfLocations=['Oculus', 'Tesco']
```

You may want to restrict the search area by changing the value of maps.RESTRICTEDTO

Create a map generator object, and pass in the list
```python
generator=MapGenerator(NamesOfLocations)
```

Decode them into a list of Location objects
```python
locations = generator.decodeLocations()
```

You may do all calculations using these objects

Location objects

| Attribute    | Meaning                                       |
| ------------ | --------------------------------------------- |
| name         | Location Name                                 |
| latitude     | Latitude                                      |
| longitude    | Longitude                                     |
| distanceTo() | Distance to another location object in metres |

To render them on a map, specify the location objects to render, in the order required
```python
generator.renderLocations(locationObjectsToRender)
```

