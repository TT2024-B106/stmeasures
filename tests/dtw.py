import matplotlib.pyplot as plt
from stmeasures.calculate.dtw import DTW
import numpy as np

def plot_trajectories(seq1, seq2, title="Comparación de Rutas"):
    seq1_array = np.array(seq1)
    seq2_array = np.array(seq2)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(seq1_array[:, 0], seq1_array[:, 1], 'b-o', label='Ruta 1')
    

    plt.plot(seq2_array[:, 0], seq2_array[:, 1], 'r-o', label='Ruta 2')
    
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            plt.plot([seq1[i][0], seq2[j][0]], 
                    [seq1[i][1], seq2[j][1]], 
                    'gray', alpha=0.1, linestyle='--')
    

    plt.title(title)
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.legend()
    plt.grid(True)
    

    plt.show()


def main():
    seq1 = [
    (19.4326, -99.1332),  # CDMX centro
    (19.4400, -99.1270),
    (19.4480, -99.1200),
    (19.4520, -99.1150),
    (19.4600, -99.1100),
    (19.4650, -99.1000),
    (19.4700, -99.0900),
    (19.4750, -99.0800),
    (19.4800, -99.0700),
    (19.4850, -99.0600),
    (19.4900, -99.0500),
    (19.4950, -99.0400),
    (19.5000, -99.0300),
    (19.5050, -99.0200),
    (19.5100, -99.0100)   # Punto final
	]


    seq2 = [
    (19.4326, -99.1332),  # Mismo punto inicial
    (19.4390, -99.1280),
    (19.4470, -99.1190),
    (19.4540, -99.1140),
    (19.4580, -99.1110),
    (19.4630, -99.1020),
    (19.4690, -99.0920),
    (19.4740, -99.0810),
    (19.4810, -99.0690),
    (19.4870, -99.0580),
    (19.4920, -99.0510),
    (19.4960, -99.0420),
    (19.5020, -99.0280),
    (19.5070, -99.0190),
    (19.5100, -99.0100)   # Mismo punto final
     ]
    
    # Crear instancia de DTW
    dtw = DTW()
    
    # Calcular distancia DTW
    distance = dtw.distance(seq1, seq2)
    print(f"Distancia DTW: {distance}")
    
    # Graficar las rutas
    plot_trajectories(seq1, seq2, f"Comparación de Rutas (DTW Distance: {distance:.2f})")

if __name__ == "__main__":
    main()
