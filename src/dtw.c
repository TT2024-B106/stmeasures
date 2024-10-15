#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "dtw.h"
#include <float.h>

double distance_between_points(const Point* point1, const Point* point2) {
    double deltaX = point2->latitude - point1->latitude;
    double deltaY = point2->longitude - point1->longitude;

    double distance = sqrt(deltaX * deltaX + deltaY * deltaY);

    return distance;
}
double** calculate_dtw_matrix(const CoordinateSequence* seq1, const CoordinateSequence* seq2) {
    int m = seq1->size; 
    int n = seq2->size;


    double** accumulatedCost = (double**)malloc(m * sizeof(double*));
    for (int i = 0; i < m; ++i) {
        accumulatedCost[i] = (double*)malloc(n * sizeof(double));
    }


    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            accumulatedCost[i][j] = 0.0;  // Inicializar a 0
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            accumulatedCost[i][j] = distance_between_points(&seq1->points[i], &seq2->points[j]);

            if (i == 0 && j == 0) {
                continue;  // Primer elemento ya inicializado
            } else if (i == 0) {
                accumulatedCost[i][j] += accumulatedCost[i][j - 1]; // Solo movimiento hacia la izquierda
            } else if (j == 0) {
                accumulatedCost[i][j] += accumulatedCost[i - 1][j]; // Solo movimiento hacia abajo
            } else {
                accumulatedCost[i][j] += fmin(
                    accumulatedCost[i - 1][j],  // Movimiento hacia abajo
                    fmin(
                        accumulatedCost[i][j - 1], // Movimiento hacia la izquierda
                        accumulatedCost[i - 1][j - 1] // Movimiento diagonal
                    )
                );
            }
        }
    }

    return accumulatedCost; 
}



#include <stdlib.h>  // Para malloc y free
#include <float.h>   // Para DBL_MAX

int** calculate_optimal_path(double** accumulatedCost, int m, int n, int* path_size) {

    int** optimalPath = (int**)malloc((m + n) * sizeof(int*)); // El tamaño máximo es m+n
    for (int i = 0; i < m + n; ++i) {
        optimalPath[i] = (int*)malloc(2 * sizeof(int)); // Cada entrada tiene dos elementos (i, j)
    }

    int i = m - 1;
    int j = n - 1;
    *path_size = 0; 

    while (i > 0 || j > 0) {
        optimalPath[*path_size][0] = i;
        optimalPath[*path_size][1] = j;
        (*path_size)++;

        double minCost = DBL_MAX;

        if (i > 0 && j > 0) {
            minCost = fmin(
                accumulatedCost[i - 1][j],          // Movimiento hacia abajo
                fmin(
                    accumulatedCost[i][j - 1],      // Movimiento hacia la izquierda
                    accumulatedCost[i - 1][j - 1]   // Movimiento diagonal
                )
            );
        }
        if (i > 0 && j <= 0) {
            minCost = fmin(minCost, accumulatedCost[i - 1][j]);     // Movimiento hacia abajo
        }
        if (j > 0 && i <= 0) {
            minCost = fmin(minCost, accumulatedCost[i][j - 1]);     // Movimiento hacia la izquierda
        }

        // Actualizamos las coordenadas según el movimiento con el costo mínimo
        if (i > 0 && j > 0 && accumulatedCost[i - 1][j - 1] == minCost) {
            i--;
            j--;
        } else if (i > 0 && accumulatedCost[i - 1][j] == minCost) {
            i--;
        } else {
            j--;
        }
    }

    // Agregar el punto (0, 0) al camino óptimo
    optimalPath[*path_size][0] = 0;
    optimalPath[*path_size][1] = 0;
    (*path_size)++;

    // Invertir el camino para que sea desde (0, 0) hasta (m-1, n-1)
    for (int k = 0; k < *path_size / 2; ++k) {
        int temp0 = optimalPath[k][0];
        int temp1 = optimalPath[k][1];
        optimalPath[k][0] = optimalPath[*path_size - 1 - k][0];
        optimalPath[k][1] = optimalPath[*path_size - 1 - k][1];
        optimalPath[*path_size - 1 - k][0] = temp0;
        optimalPath[*path_size - 1 - k][1] = temp1;
    }

    return optimalPath; // Devolver el camino óptimo
}


double calculate_cost_from_optimal_path(double** accumulatedCost, int** optimalPath, int path_size) {
    double cost = 0.0;

    for (int i = 0; i < path_size; i++) {
        int x = optimalPath[i][0]; // Obtener la fila
        int y = optimalPath[i][1]; // Obtener la columna
        cost += accumulatedCost[x][y]; // Sumar el costo acumulado
    }

    return cost;
}


double dtw_execute(const CoordinateSequence* seq1, const CoordinateSequence* seq2) {

    double** matrizCostos = calculate_dtw_matrix(seq1, seq2);

    int m = seq1->size; // Longitud de seq1
    int n = seq2->size; // Longitud de seq2


    int path_size = 0;
    int** rutaOptima = calculate_optimal_path(matrizCostos, m, n, &path_size);


    double costDTW = calculate_cost_from_optimal_path(matrizCostos, rutaOptima, path_size);


    for (int i = 0; i < m; ++i) {
        free(matrizCostos[i]);
    }
    free(matrizCostos);

    for (int i = 0; i < path_size; ++i) {
        free(rutaOptima[i]);
    }
    free(rutaOptima);

    return costDTW;
}
