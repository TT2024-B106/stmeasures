#include "lcss.h"

int is_within_threshold(double r, double s, double epsilon) {
    return fabs(r - s) <= epsilon;
}

double distance(const Trajectory *r,
                const Trajectory *s,
                double epsilon) {
    int m = r->size;
    int n = s->size;

    DoubleMatrix *dp = initialize_matrix(m + 1, n + 1, 0.0);

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (is_within_threshold(r->points[i - 1].latitude, s->points[j - 1].latitude, epsilon)
                || is_within_threshold(r->points[i - 1].longitude, s->points[j - 1].longitude, epsilon)) {
                dp->matrix[i][j] = dp->matrix[i - 1][j - 1] + 1;
            } else {
                dp->matrix[i][j] = fmax(dp->matrix[i - 1][j], dp->matrix[i][j - 1]);
            }
        }
    }

    double result = dp->matrix[m][n];
    free_matrix(dp);

    return result / fmax(m, n); // Normalize
}
