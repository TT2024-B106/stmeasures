"""Euclidean algorithm class."""

import ctypes

from stmeasures.calculate.base import BaseAlgorithm

class Euclidean(BaseAlgorithm):
    """An euclidean instance that mainly computes the euclidean algorithm
    between two trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, default: "libeuclidean"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the euclidean distance of Point 1 (1, 2) and Point 2 (3, 4)

    >>> euclidean = Euclidean() # Intializes object and loads shared library
    >>> euclidean.distance([1, 2], [3, 4])
    2.8284271247461903
    """

    def __init__(self, libname="libeuclidean") -> None:
        super().__init__(libname)

    def distance(
            self,
            p: list[float],
            q: list[float]
        ) -> float:
        """Return the euclidean distance between two trajectories.

        Parameters
        ----------
        p : list[float]
            A first vector in Euclidean n-space
        q : list[float]
            A second vector in Euclidean n-space
        """
        len_p = len(p)

        # TODO: Validation in Base class?
        #       Could be better to create a whole `validate` module

        doublearray = ctypes.c_double * len_p
        self.lib.distance.argtypes = [
            doublearray,
            doublearray,
            ctypes.c_size_t,
        ]
        self.lib.distance.restype = ctypes.c_double

        return self.lib.distance(doublearray(*p), doublearray(*q), len_p)
