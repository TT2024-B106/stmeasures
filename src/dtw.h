#ifndef DTW_H
#define DTW_H

#include "coordinates.h"

double dtw_execute(const CoordinateSequence* seq1, const CoordinateSequence* seq2);
double** calculate_dtw_matrix(const CoordinateSequence* seq1, const CoordinateSequence* seq2);
int** calculate_optimal_path(double** accumulatedCost, int m, int n, int* path_size);
double calculate_cost_from_optimal_path(double** accumulatedCost, int** optimalPath, int path_size);
double distance_between_points(const Point* point1, const Point* point2);


#endif

