#include "frechet.h"

// Helper function to convert a Point structure to an array for `distance`
void point_to_array(const Point *p, double *arr) {
    arr[0] = p->latitude;
    arr[1] = p->longitude;
}

// Helper function to initialize a 2D cache matrix
double **initialize_cache(int m, int n) {
    if (m == 0 || n == 0) {
        return NULL;
    }
    double **cache = (double **)malloc(m * sizeof(double *));
    if (!cache) {
        return NULL;
    }
    for (int i = 0; i < m; i++) {
        cache[i] = (double *)malloc(n * sizeof(double));
        if (!cache[i]) {
            for (int k = 0; k < i; k++) {
                free(cache[k]);
            }
            free(cache);
            return NULL;
        }
        for (int j = 0; j < n; j++) {
            cache[i][j] = -1.0; // Initialize all cells to -1
        }
    }
    return cache;
}

// Helper function to free the cache matrix
void free_cache(double **cache, int m) {
    for (int i = 0; i < m; i++) {
        free(cache[i]);
    }
    free(cache);
}

// Main function to compute the Fréchet distance
double frechet_execute(const Trajectory *seq1, const Trajectory *seq2) {
    int m = seq1->size;
    int n = seq2->size;

    double **cache = initialize_cache(m, n);
    if (!cache) {
        return -1.0; // Memory allocation failed
    }

    double p_arr[2] = {0.0, 0.0};
    double q_arr[2] = {0.0, 0.0};

    // Fill the cache iteratively
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            point_to_array(&seq1->points[i], p_arr);
            point_to_array(&seq2->points[j], q_arr);

            if (i == 0 && j == 0) {
                cache[i][j] = distance(p_arr, q_arr, 2);
            } else if (i > 0 && j == 0) {
                cache[i][j] = fmax(cache[i - 1][0], distance(p_arr, q_arr, 2));
            } else if (i == 0 && j > 0) {
                cache[i][j] = fmax(cache[0][j - 1], distance(p_arr, q_arr, 2));
            } else if (i > 0 && j > 0) {
                double min_prev = fmin(fmin(cache[i - 1][j], cache[i][j - 1]), cache[i - 1][j - 1]);
                cache[i][j] = fmax(min_prev, distance(p_arr, q_arr, 2));
            } else {
                cache[i][j] = DBL_MAX; // Should not happen
            }
        }
    }

    if (cache != NULL) {
        double result = cache[m - 1][n - 1];
        free_cache(cache, m);
        return result;
    } else {
        return -1.0; // Handle the error appropriately
    }
}