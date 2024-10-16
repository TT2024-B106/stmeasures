import ctypes
from stmeasures.calculate.base import BaseAlgorithm
import os

class Frechet(BaseAlgorithm):
    def __init__(self, libname="stmeasures-clib/libfrechet.so") -> None:
        super().__init__(libname)

    def distance(self, P: list[float], Q: list[float]) -> float:
        len_P = len(P) // 2  # Assuming P and Q are lists of x, y coordinates
        len_Q = len(Q) // 2
        doublearray = ctypes.c_double * len(P)
        self.lib.frechet_distance.argtypes = [doublearray, doublearray, ctypes.c_size_t, ctypes.c_size_t]
        self.lib.frechet_distance.restype = ctypes.c_double
        return self.lib.frechet_distance(doublearray(*P), doublearray(*Q), len_P, len_Q)
