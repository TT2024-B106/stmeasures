#ifndef COORDINATES_H
#define COORDINATES_H

typedef struct {
    double latitude;
    double longitude;
} Point;

typedef struct {
    Point *points;  // Apuntador a un arreglo de puntos
    size_t size;    // Tamaño del arreglo
} CoordinateSequence;

#endif

