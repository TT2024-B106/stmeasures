#include "hausdorff.h"

// Haversine distance calculation function
double haversine_distance(Point p1, Point p2) {
    const double PI = 3.141516;
    double lat1 = p1.latitude * PI / 180.0; // Convert degrees to radians
    double lon1 = p1.longitude * PI / 180.0;
    double lat2 = p2.latitude * PI / 180.0;
    double lon2 = p2.longitude * PI / 180.0;

    double dlat = lat2 - lat1;
    double dlon = lon2 - lon1;

    double a = pow(sin(dlat / 2), 2) +
               cos(lat1) * cos(lat2) * pow(sin(dlon / 2), 2);
    double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    return EARTH_RADIUS_KM * c; // Distance in kilometers
}

// Hausdorff distance calculation function between two trajectories
double hausdorff_execute(Trajectory* traj1, Trajectory* traj2) {
    double max_dist_p_to_q = 0.0;
    double max_dist_q_to_p = 0.0;

    // Calculate the maximum distance from traj1 to traj2
    for (size_t i = 0; i < traj1->size; i++) {
        double min_dist = DBL_MAX;
        for (size_t j = 0; j < traj2->size; j++) {
            double dist = haversine_distance(traj1->points[i], traj2->points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
        if (min_dist > max_dist_p_to_q) {
            max_dist_p_to_q = min_dist;
        }
    }

    // Calculate the maximum distance from traj2 to traj1
    for (size_t i = 0; i < traj2->size; i++) {
        double min_dist = DBL_MAX;
        for (size_t j = 0; j < traj1->size; j++) {
            double dist = haversine_distance(traj2->points[i], traj1->points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
        if (min_dist > max_dist_q_to_p) {
            max_dist_q_to_p = min_dist;
        }
    }

    // The Hausdorff distance is the maximum of the two maximum distances
    return fmax(max_dist_p_to_q, max_dist_q_to_p);
}
