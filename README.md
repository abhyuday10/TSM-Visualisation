# TSM-Visualisation
Visualising the TSM problem in the context of local pubs.

## Installing dependencies
```
git clone https://github.com/abhyuday10/TSM-Visualisation
pip install -r requirements.txt
```

## Usage Details

1. Create a list of locations
    ```python
    from map import *
    NamesOfLocations = ['Oculus', 'Tesco']
    ```
You may want to restrict the search area by changing the value of maps.RESTRICTEDTO

2. Create a map generator object, and pass in the list
    ```python
    generator = MapGenerator(NamesOfLocations)
    ```

3. Decode them into a list of Location objects
    ```python
    locations = generator.decodeLocations()
    ```

    You may do all calculations using these objects

    #### Location Object
    | Attribute    | Meaning                                       |
    | ------------ | --------------------------------------------- |
    | name         | Location Name                                 |
    | latitude     | Latitude                                      |
    | longitude    | Longitude                                     |
    | distanceTo() | Distance to another location object in metres |

4. To render them on a map, specify the location objects to render, in the order required
    ```python
    generator.renderLocations(locationObjectsToRender)
    ```

