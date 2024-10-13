import ctypes
import os
from stmeasures.calculate.base import BaseAlgorithm


class Point(ctypes.Structure):
    """Represents a point in a two-dimensional space.

    Attributes
    ----------
    latitude : float
        The latitude of the point.
    longitude : float
        The longitude of the point.
    """
    _fields_ = [("latitude", ctypes.c_double), ("longitude", ctypes.c_double)]

class CoordinateSequence(ctypes.Structure):
    """Represents a sequence of points in a two-dimensional space.

    Attributes
    ----------
    points : ctypes.POINTER(Point)
        A pointer to an array of points.
    size : size_t
        The number of points in the sequence.
    """
    _fields_ = [("points", ctypes.POINTER(Point)), ("size", ctypes.c_size_t)]

class DTW(BaseAlgorithm):
    """A DTW class that implements the Dynamic Time Warping algorithm
    between two sequences of coordinates.

    Parameters
    ----------
    libname : str, default: "libdtw"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the DTW distance between two sequences of coordinates:

    >>> dtw = DTW()  # Initializes the object and loads the shared library
    >>> seq1 = [(1.0, 1.0), (2.0, 2.0)]
    >>> seq2 = [(1.5, 1.5), (3.0, 3.0)]
    >>> dtw.distance(seq1, seq2)
    1.4142135623730951  # Example expected result (adjust based on your implementation)
    """

    def __init__(self, libname="libdtw") -> None:
        """Initializes the DTW class and loads the shared library.

        Parameters
        ----------
        libname : str, optional
            The name of the shared library file (default is "libdtw").
        """
        super().__init__(libname)


        self.lib.dtw_execute.argtypes = [ctypes.POINTER(CoordinateSequence), ctypes.POINTER(CoordinateSequence)]
        self.lib.dtw_execute.restype = ctypes.c_double

    def distance(self, seq1: list[tuple[float, float]], seq2: list[tuple[float, float]]) -> float:
        """Returns the DTW distance between two sequences of coordinates.

        Parameters
        ----------
        seq1 : list[tuple[float, float]]
            The first sequence of coordinates (latitude, longitude).
        seq2 : list[tuple[float, float]]
            The second sequence of coordinates (latitude, longitude).

        Returns
        -------
        float
            The DTW distance between the two sequences of coordinates.

        Raises
        ------
        ValueError
            If either of the sequences is empty or improperly formatted.

        Examples
        --------
        >>> seq1 = [(1.0, 1.0), (2.0, 2.0)]
        >>> seq2 = [(1.5, 1.5), (3.0, 3.0)]
        >>> dtw = DTW()
        >>> dtw.distance(seq1, seq2)
        1.4142135623730951  # Example expected result (adjust based on your implementation)
        """

        if not seq1 or not seq2:
            raise ValueError("Sequences cannot be empty.")


        seq1_points = (Point * len(seq1))(*[Point(lat, lon) for lat, lon in seq1])
        seq2_points = (Point * len(seq2))(*[Point(lat, lon) for lat, lon in seq2])

        seq1_c = CoordinateSequence(seq1_points, len(seq1))
        seq2_c = CoordinateSequence(seq2_points, len(seq2))


        return self.lib.dtw_execute(ctypes.byref(seq1_c), ctypes.byref(seq2_c))

