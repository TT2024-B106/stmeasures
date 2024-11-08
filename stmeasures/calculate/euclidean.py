"""Euclidean algorithm class."""

import ctypes

from stmeasures.validation import validate_euclidean
from stmeasures.calculate.base import BaseAlgorithm

class Euclidean(BaseAlgorithm):
    """
    An instance for calculating the Euclidean distance between two lists of
    floats (trajectories).

    :param libname: 
        The file name of the compiled shared library.
    :type libname: str, default "libeuclidean"

    :example:
        Calculating the Euclidean distance between two points:

        >>> euclidean = Euclidean()  # Initializes object and loads shared library
        >>> euclidean.distance([1, 2], [3, 4])
        2.8284271247461903
    """

    def __init__(self, libname="libeuclidean") -> None:
        """
        Initializes the Euclidean distance calculator with a specified library
        name.

        :param libname: 
            The file name of the compiled shared library.
        :type libname: str, default "libeuclidean"
        """
        super().__init__(libname)

    def distance(self, p: list[float], q: list[float]) -> float:
        """
        Calculates the Euclidean distance between two trajectories.

        :param p:
            The first vector in Euclidean n-space.
        :type p: list[float]

        :param q:
            The second vector in Euclidean n-space.
        :type q: list[float]

        :return: The Euclidean distance between the two input vectors.
        :rtype: float

        :raises ValueError:
            - if `p` or `q` is not a list of floats or if they do not have the
              same length

        :raises RuntimeError:
            - if there is an error with the C library call
            - if an unexpected error occurs during execution

        :example:
            Calculating the Euclidean distance between two vectors:

            >>> euclidean = Euclidean()
            >>> euclidean.distance([1.0, 2.0], [3.0, 4.0])
            2.8284271247461903
        """
        try:
            len_p = len(p)

            validate_euclidean(p, q)

            doublearray = ctypes.c_double * len_p
            self.lib.distance.argtypes = [
                doublearray,
                doublearray,
                ctypes.c_size_t,
            ]
            self.lib.distance.restype = ctypes.c_double

            return self.lib.distance(doublearray(*p), doublearray(*q), len_p)
        except ValueError as ve:
            print(ve)
            raise RuntimeError(
                f"Invalid parameters p:{p}, q:{q} in {self.__module__}"
            ) from ve
        except ctypes.ArgumentError as ae:
            print(ae)
            raise RuntimeError(
                f"Argument error in C shared library call {self._libpath}"
            ) from ae
        except Exception as e:
            print(e)
            raise RuntimeError(
                f"Unexpected error in {self.__module__}"
            ) from e
