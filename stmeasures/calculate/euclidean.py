import ctypes

from stmeasures.calculate.base import BaseAlgorithm

class Euclidean(BaseAlgorithm):
    def __init__(self, libname="libeuclidean") -> None:
        super().__init__(libname)

    def distance(
            self,
            p: list[float],
            q: list[float]
        ) -> float:
        len_p = len(p)

        # TODO: Validation in Base class?

        doublearray = ctypes.c_double * len_p
        self.lib.distance.argtypes = [
            doublearray,
            doublearray,
            ctypes.c_size_t,
        ]
        self.lib.distance.restype = ctypes.c_double

        return self.lib.distance(doublearray(*p), doublearray(*q), len_p)
