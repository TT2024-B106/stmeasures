#ifndef FRECHET_H
#define FRECHET_H

#include "trajectory.h"  // For the Trajectory structure
#include "euclidean.h"   // For the Euclidean distance function
#include <float.h>       // For DBL_MAX
#include <math.h>        // For math functions like sqrt, pow, fmin, fmax
#include <stdlib.h>      // For memory allocation functions

// Main function to compute the Fréchet distance
double frechet_execute(const Trajectory *seq1, const Trajectory *seq2);

// Helper functions for internal use (if needed externally, they can be exposed here too)
double **initialize_cache(int m, int n); // Initializes the dynamic programming cache
void free_cache(double **cache, int m);  // Frees the allocated cache memory

#endif