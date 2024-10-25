#ifndef DTW_H
#define DTW_H

#include "trayectory.h"
#include "matrix.h"

double dtw_execute(const Trayectory *seq1,
                   const Trayectory *seq2);

DoubleMatrix *calculate_dtw_matrix(const Trayectory *seq1,
                                   const Trayectory *seq2);

int **calculate_optimal_path(DoubleMatrix *accumulatedCost, int *path_size);

double calculate_cost_from_optimal_path(DoubleMatrix *accumulatedCost,
                                        int **optimalPath, int path_size);

#endif
