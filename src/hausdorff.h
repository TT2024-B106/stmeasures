#ifndef HAUSDORFF_H
#define HAUSDORFF_H

#include <stdio.h>
#include <math.h>
#include <float.h>
#include "trajectory.h"  // For the Trajectory structure

// Earth's radius in kilometers
#define EARTH_RADIUS_KM 6371.0

// Function to calculate the Haversine distance between two points
double haversine_distance(Point p1, Point p2);

// Function to calculate the Hausdorff distance between two trajectories
double hausdorff_execute(Trajectory* traj1, Trajectory* traj2);

#endif // HAUSDORFF_H