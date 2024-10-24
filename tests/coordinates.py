import ctypes

class Point(ctypes.Structure):
    _fields_ = [("latitude", ctypes.c_double), ("longitude", ctypes.c_double)]

class CoordinateSequence(ctypes.Structure):
    _fields_ = [("points", ctypes.POINTER(Point)), ("size", ctypes.c_size_t)]
