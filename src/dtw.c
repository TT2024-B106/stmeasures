#include "dtw.h"
#include <float.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double distance_between_points(const Point *point1, const Point *point2) {
  double deltaX = point2->latitude - point1->latitude;
  double deltaY = point2->longitude - point1->longitude;

  double distance = sqrt(deltaX * deltaX + deltaY * deltaY);

  return distance;
}

double **calculate_dtw_matrix(const CoordinateSequence *seq1,
                              const CoordinateSequence *seq2) {
  int m = seq1->size;
  int n = seq2->size;

  // Asignar memoria para la matriz de costos acumulados
  double **accumulatedCost = (double **)malloc(m * sizeof(double *));
  if (accumulatedCost == NULL) {
    fprintf(stderr, "Error al asignar memoria para accumulatedCost\n");
    return NULL;
  }

  for (int i = 0; i < m; ++i) {
    accumulatedCost[i] = (double *)malloc(n * sizeof(double));
    if (accumulatedCost[i] == NULL) {
      fprintf(stderr,
              "Error al asignar memoria para la fila %d de accumulatedCost\n",
              i);
      // Liberar la memoria asignada previamente
      for (int k = 0; k < i; ++k) {
        free(accumulatedCost[k]);
      }
      free(accumulatedCost);
      return NULL;
    }
  }

  // Inicializar la matriz de costos a 0
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      accumulatedCost[i][j] = 0.0;
    }
  }

  // Calcular la matriz de costos acumulados
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      accumulatedCost[i][j] =
          distance_between_points(&seq1->points[i], &seq2->points[j]);

      if (i == 0 && j == 0) {
        continue; // Primer elemento ya inicializado
      } else if (i == 0) {
        accumulatedCost[i][j] +=
            accumulatedCost[i][j - 1]; // Solo movimiento hacia la izquierda
      } else if (j == 0) {
        accumulatedCost[i][j] +=
            accumulatedCost[i - 1][j]; // Solo movimiento hacia abajo
      } else {
        accumulatedCost[i][j] += fmin(
            accumulatedCost[i - 1][j],         // Movimiento hacia abajo
            fmin(accumulatedCost[i][j - 1],    // Movimiento hacia la izquierda
                 accumulatedCost[i - 1][j - 1] // Movimiento diagonal
                 ));
      }
    }
  }

  return accumulatedCost;
}

int **calculate_optimal_path(double **accumulatedCost, int m, int n,
                             int *path_size) {

  int **optimalPath =
      (int **)malloc((m + n) * sizeof(int *)); // El tamaño máximo es m+n
  if (optimalPath == NULL) {
    fprintf(stderr, "Error al asignar memoria para el camino óptimo\n");
    return NULL;
  }

  *path_size = 0;
  int max_path_size = m + n - 1; // Tamaño máximo posible del camino

  // Inicializar todos los elementos de optimalPath
  for (int i = 0; i < max_path_size; ++i) {
    optimalPath[i] = (int *)malloc(2 * sizeof(int));
    if (optimalPath[i] == NULL) {
      fprintf(stderr, "Error al asignar memoria para el punto óptimo %d\n", i);
      // Liberar la memoria asignada previamente
      for (int k = 0; k < i; ++k) {
        free(optimalPath[k]);
      }
      free(optimalPath);
      return NULL;
    }
  }

  int i = m - 1;
  int j = n - 1;

  while (i >= 0 || j >= 0) {
    if (*path_size >= max_path_size) {
      // Manejar error: el camino es más largo de lo esperado
      for (int k = 0; k < max_path_size; ++k) {
        free(optimalPath[k]);
      }
      free(optimalPath);
      return NULL;
    }

    optimalPath[*path_size][0] = i;
    optimalPath[*path_size][1] = j;
    (*path_size)++;

    if (i == 0 && j == 0) {
      break;
    }

    double minCost = DBL_MAX;

    if (i > 0 && j > 0) {
      minCost =
          fmin(accumulatedCost[i - 1][j],      // Movimiento hacia abajo
               fmin(accumulatedCost[i][j - 1], // Movimiento hacia la izquierda
                    accumulatedCost[i - 1][j - 1] // Movimiento diagonal
                    ));
    }
    if (i > 0 && j == 0) {
      minCost = accumulatedCost[i - 1][j]; // Movimiento hacia abajo
    }
    if (j > 0 && i == 0) {
      minCost = accumulatedCost[i][j - 1]; // Movimiento hacia la izquierda
    }

    // Actualizamos las coordenadas según el movimiento con el costo mínimo
    if (i > 0 && j > 0 && accumulatedCost[i - 1][j - 1] == minCost) {
      i--;
      j--;
    } else if (i > 0 && accumulatedCost[i - 1][j] == minCost) {
      i--;
    } else if (j > 0) {
      j--;
    }
  }

  // Invertir el camino para que sea desde (0, 0) hasta (m-1, n-1)
  for (int k = 0; k < *path_size / 2; ++k) {
    int temp0 = optimalPath[k][0];
    int temp1 = optimalPath[k][1];
    optimalPath[k][0] = optimalPath[*path_size - 1 - k][0];
    optimalPath[k][1] = optimalPath[*path_size - 1 - k][1];
    optimalPath[*path_size - 1 - k][0] = temp0;
    optimalPath[*path_size - 1 - k][1] = temp1;
  }

  return optimalPath;
}

double calculate_cost_from_optimal_path(double **accumulatedCost,
                                        int **optimalPath, int path_size) {
  double cost = 0.0;

  for (int i = 0; i < path_size; i++) {
    int x = optimalPath[i][0];     // Obtener la fila
    int y = optimalPath[i][1];     // Obtener la columna
    cost += accumulatedCost[x][y]; // Sumar el costo acumulado
  }

  return cost;
}

double dtw_execute(const CoordinateSequence *seq1,
                   const CoordinateSequence *seq2) {

  double **matrizCostos = calculate_dtw_matrix(seq1, seq2);
  if (matrizCostos == NULL) {
    fprintf(stderr, "Error al calcular la matriz de costos DTW\n");
    return -1.0; // Devolver un valor de error
  }

  int m = seq1->size;
  int n = seq2->size;

  int path_size = 0;
  int **rutaOptima = calculate_optimal_path(matrizCostos, m, n, &path_size);
  if (rutaOptima == NULL) {
    fprintf(stderr, "Error al calcular la ruta óptima\n");
    // Liberar la matriz de costos antes de salir
    for (int i = 0; i < m; ++i) {
      free(matrizCostos[i]);
    }
    free(matrizCostos);
    return -1.0; // Devolver un valor de error
  }

  double costDTW =
      calculate_cost_from_optimal_path(matrizCostos, rutaOptima, path_size);

  // Liberar la matriz de costos
  for (int i = 0; i < m; ++i) {
    free(matrizCostos[i]);
  }
  free(matrizCostos);

  // Liberar la ruta óptima
  for (int i = 0; i < path_size; ++i) {
    free(rutaOptima[i]);
  }
  free(rutaOptima);

  return costDTW;
}
