#include "hausdorff.h"

double point_set_distance(const double *p, const double *q, size_t p_size, size_t q_size) {
    double max_min_distance = 0.0;

    for (size_t i = 0; i < p_size; ++i) {
        double min_distance = DBL_MAX;

        for (size_t j = 0; j < q_size; ++j) {
            double diff = p[i] - q[j];
            double distance = diff * diff;

            if (distance < min_distance) {
                min_distance = distance;
            }
        }

        if (min_distance > max_min_distance) {
            max_min_distance = min_distance;
        }
    }

    return sqrt(max_min_distance);
}

double hausdorff_distance(const double *p, const double *q, size_t p_size, size_t q_size) {
    double d_pq = point_set_distance(p, q, p_size, q_size);
    double d_qp = point_set_distance(q, p, q_size, p_size);

    return fmax(d_pq, d_qp);
}
