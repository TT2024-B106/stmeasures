import json
import os
import webbrowser
import folium
from stmeasures.calculate.dtw import DTW
from stmeasures.objects.TrajectoryHandler import TrajectoryHandler

def retrieve_coordinates(json_file, n):
    """
    Función que recupera 'n' arreglos de coordenadas de un archivo JSON.
    
    :param json_file: Ruta al archivo .json.
    :param n: Número de arreglos de coordenadas a recuperar.
    :return: Lista de 'n' listas de coordenadas.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    coordinate_sets = []
    
    for feature_collection in data['data'][:n]:
        for feature in feature_collection['features']:
            coords = feature['geometry']['coordinates']
            coordinate_sets.append(coords)
    
    return coordinate_sets

def plot_and_calculate_dtw(coords_list):
    """
    Plotea las coordenadas usando Folium y calcula la distancia DTW entre las secuencias de coordenadas.
    
    :param coords_list: Lista de listas de coordenadas.
    """
    handler = TrajectoryHandler()
    
    trajectories = [handler.create_trajectory(coords) for coords in coords_list]
    
    labels = [f"Trayectoria {i+1}" for i in range(len(trajectories))]
    mapa = handler.plot_folium(
        trajectories=trajectories,
        labels=labels,
        zoom_start=12
    )
    
    output_file = 'mapa_dtw2.html'
    mapa.save(output_file)
    
    file_path = os.path.abspath(output_file)
    print(f"Abriendo mapa en el navegador... {file_path}")
    webbrowser.open('file://' + file_path)
    
    dtw = DTW()
    for i in range(len(coords_list) - 1):
        distance = dtw.distance(coords_list[i], coords_list[i+1])
        print(f"Distancia DTW entre Trayectoria {i+1} y Trayectoria {i+2}: {distance}")

def main():
    json_file = 'ECATEPEC.json'  # Asegúrate de tener la ruta correcta al archivo JSON
    n = 15  # Número de conjuntos de coordenadas a recuperar
    
    coords_list = retrieve_coordinates(json_file, n)
    
    #for i, coords in enumerate(coords_list):
    #    print(f"Coordenadas {i+1}: {coords}")
    
    plot_and_calculate_dtw(coords_list)

if __name__ == "__main__":
    try:
        main()
        print("\nOperación completada exitosamente!")
    except Exception as e:
        print(f"\nError: {str(e)}")

