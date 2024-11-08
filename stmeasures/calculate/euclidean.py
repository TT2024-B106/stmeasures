"""Euclidean algorithm class."""

import ctypes

from stmeasures.validation import validate_euclidean
from stmeasures.calculate.base import BaseAlgorithm
from stmeasures.objects.cstructures import Trajectory, Point

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

        self.lib.distance.argtypes = [ctypes.POINTER(Trajectory), ctypes.POINTER(Trajectory)]
        self.lib.distance.restype = ctypes.c_double

    def distance(
            self,
            p: list[tuple[float, float]],
            q: list[tuple[float, float]]
        ) -> float:
        """
        Calculates the Euclidean distance between two trajectories.

        :param p:
            The first vector in Euclidean n-space.
        :type p: list[tuple[float, float]

        :param q:
            The second vector in Euclidean n-space.
        :type q: list[tuple[float, float]

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
            validate_euclidean(p, q)

            _len = len(p)

            points_p = (Point * _len)(*[Point(lat, lon) for lat, lon in p])
            points_q = (Point * _len)(*[Point(lat, lon) for lat, lon in q])

            trajectory_p = Trajectory(points_p, _len)
            trajectory_q = Trajectory(points_q, _len)

            return self.lib.distance(
                ctypes.byref(trajectory_p),
                ctypes.byref(trajectory_q)
            )
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
