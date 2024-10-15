import ctypes
import os
from stmeasures.calculate.base import BaseAlgorithm


class Point(ctypes.Structure):
    _fields_ = [("latitude", ctypes.c_double), ("longitude", ctypes.c_double)]

class CoordinateSequence(ctypes.Structure):
    _fields_ = [("points", ctypes.POINTER(Point)), ("size", ctypes.c_size_t)]

class DTW(BaseAlgorithm):
    """Una clase DTW que implementa el algoritmo Dynamic Time Warping
    entre dos secuencias de coordenadas.
    """

    def __init__(self, libname="libdtw") -> None:
        super().__init__(libname)


        self.lib.dtw_execute.argtypes = [ctypes.POINTER(CoordinateSequence), ctypes.POINTER(CoordinateSequence)]
        self.lib.dtw_execute.restype = ctypes.c_double

    def distance(self, seq1: list[tuple[float, float]], seq2: list[tuple[float, float]]) -> float:
        """Retorna la distancia DTW entre dos secuencias de coordenadas.
        """

        seq1_points = (Point * len(seq1))(*[Point(lat, lon) for lat, lon in seq1])
        seq2_points = (Point * len(seq2))(*[Point(lat, lon) for lat, lon in seq2])

        seq1_c = CoordinateSequence(seq1_points, len(seq1))
        seq2_c = CoordinateSequence(seq2_points, len(seq2))


        return self.lib.dtw_execute(ctypes.byref(seq1_c), ctypes.byref(seq2_c))

