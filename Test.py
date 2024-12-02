import stmeasures
#import stmeasures.objects.abstractions as abstractions
import geojsonio
import json


# Cargar el archivo GeoJSON
geojson_obj = stmeasures.read_file("ECATEPEC.json")

# Top5 = abstractions.
geojsonio.display(json.dumps(stmeasures.get_geojsonio_trajectory(geojson_obj[6])))
