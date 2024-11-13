# stmeasures/read.py
import json
from stmeasures.objects.abstractions import GeoJSON

def file(filepath: str) -> GeoJSON:
    """
    Reads a GeoJSON file and returns a `GeoJSON` object.

    This function takes the path to a GeoJSON file, loads its contents, and 
    returns a `GeoJSON` object initialized with the data from the file. The 
    returned object can then be used to extract trajectories or perform 
    other operations on the data.

    :param filepath: The path to the GeoJSON file to read.
    :type filepath: str
    :return: A `GeoJSON` object containing the data from the file.
    :rtype: GeoJSON
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    return GeoJSON(data)
