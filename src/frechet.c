#include "frechet.h"
#include <math.h>
#include <float.h>

double min3(double a, double b, double c) {
    if (a <= b && a <= c) return a;
    if (b <= a && b <= c) return b;
    return c;
}

double ca(int i, int j, const double *P, const double *Q, double **c) {
    if (c[i][j] > -1) {
        return c[i][j];
    }
    if (i == 0 && j == 0) {
        c[i][j] = hypot(P[0] - Q[0], P[1] - Q[1]);
    } else if (i > 0 && j == 0) {
        c[i][j] = fmax(ca(i-1, 0, P, Q, c), hypot(P[2*i] - Q[0], P[2*i+1] - Q[1]));
    } else if (i == 0 && j > 0) {
        c[i][j] = fmax(ca(0, j-1, P, Q, c), hypot(P[0] - Q[2*j], P[1] - Q[2*j+1]));
    } else if (i > 0 && j > 0) {
        c[i][j] = fmax(min3(ca(i-1, j, P, Q, c), ca(i-1, j-1, P, Q, c), ca(i, j-1, P, Q, c)),
                       hypot(P[2*i] - Q[2*j], P[2*i+1] - Q[2*j+1]));
    } else {
        c[i][j] = DBL_MAX;
    }
    return c[i][j];
}

double frechet_distance(const double *P, const double *Q, size_t m, size_t n) {
    double **c = (double **)malloc(m * sizeof(double *));
    for (size_t i = 0; i < m; i++) {
        c[i] = (double *)malloc(n * sizeof(double));
        for (size_t j = 0; j < n; j++) {
            c[i][j] = -1.0;
        }
    }
    double result = ca(m-1, n-1, P, Q, c);
    for (size_t i = 0; i < m; i++) {
        free(c[i]);
    }
    free(c);
    return result;
}
