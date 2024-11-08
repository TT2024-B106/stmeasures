#include "euclidean.h"

double distance(const Trajectory *p, const Trajectory *q) {
    double sum_of_squares = 0.0;

    for (size_t i = 0; i < p->size; ++i) {
        double lat_diff = p->points[i].latitude - q->points[i].latitude;
        double lon_diff = p->points[i].longitude - q->points[i].longitude;
        sum_of_squares += (lat_diff * lat_diff) + (lon_diff * lon_diff);
    }

    return sqrt(sum_of_squares);
}
