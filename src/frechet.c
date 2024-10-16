// frechet.c
#include "frechet.h"
#include <math.h>
#include <stdlib.h>

// Function to calculate Euclidean distance between two points
static double distance_between_points(const double *p, const double *q) {
    double dx = p[0] - q[0];
    double dy = p[1] - q[1];
    return sqrt(dx * dx + dy * dy);
}

// Global cache for memoization
static double **ca;

// Recursive function to compute Frechet distance
static double c_recursive(int i, int j, const double *curve1, size_t size1, const double *curve2, size_t size2) {
    if (ca[i][j] > -1) {
        return ca[i][j];
    } else {
        double dist = distance_between_points(&curve1[2 * i], &curve2[2 * j]);
        if (i == 0 && j == 0) {
            ca[i][j] = dist;
        } else if (i > 0 && j == 0) {
            ca[i][j] = fmax(c_recursive(i - 1, 0, curve1, size1, curve2, size2), dist);
        } else if (i == 0 && j > 0) {
            ca[i][j] = fmax(c_recursive(0, j - 1, curve1, size1, curve2, size2), dist);
        } else if (i > 0 && j > 0) {
            double min_prev = fmin(
                fmin(c_recursive(i - 1, j, curve1, size1, curve2, size2),
                     c_recursive(i - 1, j - 1, curve1, size1, curve2, size2)),
                c_recursive(i, j - 1, curve1, size1, curve2, size2)
            );
            ca[i][j] = fmax(min_prev, dist);
        } else {
            ca[i][j] = INFINITY;
        }
    }
    return ca[i][j];
}

double frechet_distance(const double *curve1, size_t size1, const double *curve2, size_t size2) {
    // Allocate memory for cache
    ca = (double **)malloc(size1 * sizeof(double *));
    for (size_t i = 0; i < size1; ++i) {
        ca[i] = (double *)malloc(size2 * sizeof(double));
        for (size_t j = 0; j < size2; ++j) {
            ca[i][j] = -1.0;
        }
    }

    // Compute Frechet distance
    double result = c_recursive(size1 - 1, size2 - 1, curve1, size1, curve2, size2);

    // Free allocated memory
    for (size_t i = 0; i < size1; ++i) {
        free(ca[i]);
    }
    free(ca);

    return result;
}
