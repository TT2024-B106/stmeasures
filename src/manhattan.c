#include "manhattan.h"

double distance(const double *p, const double *q, size_t size)
{
    double sum_of_diffs = 0.0;

    for (size_t i = 0; i < size; ++i) {
        sum_of_diffs += fabs(p[i] - q[i]);
    }

    return sum_of_diffs;
}
