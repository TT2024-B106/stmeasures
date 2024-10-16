// frechet.h
#ifndef FRECHET_H
#define FRECHET_H

#include <stddef.h>

// Function to compute the Frechet distance between two curves
double frechet_distance(const double *curve1, size_t size1, const double *curve2, size_t size2);

#endif // FRECHET_H
