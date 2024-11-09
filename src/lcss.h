#ifndef LCSS_H
#define LCSS_H

#include <stdlib.h>
#include <math.h>
#include "trajectory.h"
#include "matrix.h"

double distance(const Trajectory *r, 
                const Trajectory *s,
                double epsilon);

#endif

