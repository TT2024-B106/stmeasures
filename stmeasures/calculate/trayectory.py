import ctypes
class Point(ctypes.Structure):
    """
    Represents a geographical point with latitude and longitude coordinates.

    Attributes
    ----------
    latitude : ctypes.c_double
        Latitude of the point.
    longitude : ctypes.c_double
        Longitude of the point.
    """
    _fields_ = [("latitude", ctypes.c_double), ("longitude", ctypes.c_double)]


class Trayectory(ctypes.Structure):
    """
    Represents a sequence of geographical points.

    Attributes
    ----------
    points : ctypes.POINTER(Point)
        A pointer to an array of `Point` structures.
    size : ctypes.c_size_t
        The size of the coordinate sequence (number of points).
    """
    _fields_ = [("points", ctypes.POINTER(Point)), ("size", ctypes.c_size_t)]
