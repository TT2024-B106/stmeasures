#ifndef ED_H
#define ED_H

#include "manhattan.h"
#include "math_utils.h"

double edrs_distance(
    const double *r,
    const double *s,
    size_t size_r,
    size_t size_s,
    double sigma,
    double cost_del,
    double cost_ins,
    double subcost_outside_sigma,
    double subcost_within_sigma
);

double erp(
    const double *r,
    const double *s,
    size_t size_r,
    size_t size_s,
    double g
);

#endif
