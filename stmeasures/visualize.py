"""Visualize module."""

def _swap_coordinates(coords):
    """
    Swap latitude and longitude for each coordinate tuple in a trajectory.

    This function takes a list of coordinates, where each coordinate is represented 
    as a tuple of (latitude, longitude), and returns the list with the order swapped 
    to (longitude, latitude). This is often required for proper visualization in 
    some mapping libraries that expect coordinates in the (longitude, latitude) order.

    :param coords: List of coordinate tuples in (latitude, longitude) format.
    :type coords: list[list[float, float]]
    :return: List of coordinates in (longitude, latitude) format.
    :rtype: list[list[float, float]]
    """
    return [[lon, lat] for lat, lon in coords]

def get_geojsonio_trajectory(trajectory_data):
    """
    Convert a single trajectory to a GeoJSON LineString format.

    This function converts a single trajectory, represented as a dictionary with 
    trajectory details, into the GeoJSON format. The resulting GeoJSON is in the 
    form of a `LineString`, with coordinates swapped to (longitude, latitude) format.

    :param trajectory_data: A dictionary with trajectory details, including 'coordinates'.
    :type trajectory_data: dict
    :return: GeoJSON dictionary for the trajectory in LineString format.
    :rtype: dict
    """
    geojson = {
        "type": "LineString",
        "coordinates": _swap_coordinates(trajectory_data['coordinates'])
    }
    return geojson

def get_geojson_trajectories(geojson_obj):
    """
    Convert all trajectories to GeoJSON FeatureCollection format.

    This function takes a `GeoJSON` object containing multiple trajectories and 
    converts them into a GeoJSON `FeatureCollection` format. Each trajectory is 
    represented as a `Feature` with a `LineString` geometry and properties such as 
    the trajectory's 'id' and 'timestamp'.

    :param geojson_obj: GeoJSON object containing multiple trajectories.
    :type geojson_obj: GeoJSON
    :return: GeoJSON FeatureCollection for all trajectories.
    :rtype: dict
    """
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for trajectory_data in geojson_obj.trajectories:
        geojson['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": (trajectory_data['coordinates'])
            },
            "properties": {
                "id": trajectory_data['id'],
                "timestamp": trajectory_data['timestamp']
            }
        })
    return geojson
