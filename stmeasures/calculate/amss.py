"""AMSS algorithm class."""

import ctypes
import warnings

from stmeasures.validation import validate_trajectory # TODO: Validate AMSS
from stmeasures.calculate.base import BaseAlgorithm
from stmeasures.objects.cstructures import Trajectory, Point # TODO: Implement

class AMSS(BaseAlgorithm):
    """
    A class to compute the Angular Metric for Shape Similarity (AMSS) algorithm
    between two trajectory-like lists of floats.

    :param libname: The file name of the compiled shared library.
    :type libname: str, optional, default is "libamss"

    :example:

    Calculating the AMSS distance between two points, (1, 2) and (3, 4):

    >>> amss = AMSS()  # Initializes object and loads shared library
    >>> amss.distance([(1, 2)], [(3, 4)])
    0.5
    """

    def __init__(self, libname="libamss") -> None:
        super().__init__(libname)

    def distance(
        self,
        r: list[tuple[float, float]],
        s: list[tuple[float, float]],
    ) -> float:
        """
        Calculate the AMSS distance between two trajectories.

        :param r: First trajectory, a list of (latitude, longitude) tuples.
        :type r: list[tuple[float, float]]
        :param s: Second trajectory, a list of (latitude, longitude) tuples.
        :type s: list[tuple[float, float]]

        :raises ValueError: If the trajectories or sigma are invalid.
        :raises RuntimeError: If a ctypes error occurs.

        :return: AMSS distance between the two trajectories.
        :rtype: float
        """
        try:
            validate_trajectory(r)
            validate_trajectory(s)

            _r = [r_value for _tuple in r for r_value in _tuple]
            _s = [s_value for _tuple in s for s_value in _tuple]

            # validate_amss(_r, _s)

            return self._distance(_r, _s)
        except ValueError as ve:
            print(ve)
            raise RuntimeError(
                f"Invalid parameters r:{r}, s:{s} in {self.__module__}"
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

    def _distance(
        self,
        r: list[float],
        s: list[float],
    ) -> float:
        """
        Internal method to calculate the AMSS distance between two flattened 
        trajectories.

        :param r: Flattened list representing the first trajectory.
        :type r: list[float]
        :param s: Flattened list representing the second trajectory.
        :type s: list[float]
        :param sigma: Threshold to detect matching elements, defaults to 1.
        :type sigma: float, optional

        :raises DeprecationWarning: This method is deprecated since it's not
        using cstructures.

        :return: AMSS distance between the two trajectories.
        :rtype: float
        """
        warnings.warn('Method not using cstructures', DeprecationWarning)

        len_r, len_s = len(r), len(s)

        r_array = ctypes.c_double * len_r
        s_array = ctypes.c_double * len_s

        self.lib.amss_distance.argtypes = [
            r_array,
            s_array,
            ctypes.c_size_t,
            ctypes.c_size_t,
        ]
        self.lib.amss_distance.restype = ctypes.c_double

        return self.lib.amss_distance(
            r_array(*r),
            s_array(*s),
            len_r,
            len_s,
        )
