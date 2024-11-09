"""LCSS algorithm class."""

import ctypes

from stmeasures.calculate.base import BaseAlgorithm
from stmeasures.objects.cstructures import Trajectory, Point

class LCSS(BaseAlgorithm):
    """A LCSS instance that mainly computes the Longest Common Subsequences
    (LCSS) algorithm between two trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, default: "liblcss"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the LCSS distance of Point 1 (1, 2) and Point 2 (3, 4)

    >>> lcss = LCSS() # Intializes object and loads shared library
    >>> lcss.distance([1,2],[3,4])
    0.5
    """

    def __init__(self, libname="liblcss") -> None:
        super().__init__(libname)

        self.lib.distance.argtypes = [
            ctypes.POINTER(Trajectory),
            ctypes.POINTER(Trajectory)
        ]
        self.lib.distance.restype = ctypes.c_double

    def distance(
            self,
            r: list[tuple[float, float]],
            s: list[tuple[float, float]],
            sigma: float = 1
        ) -> float:
        """Return the LCSS distance between two trajectories.

        Parameters
        ----------
        r : list[float]
            A first vector in m-space.
        s : list[float]
            A second vector in n-space.
        sigma : float, default: 1.0
            A threshold to detect elements matching.
        """
        len_r, len_s = len(r), len(s)

        # TODO: Validate in `validate` module

        points_r = (Point * len_r)(*[Point(lat, lon) for lat, lon in r])
        points_s = (Point * len_s)(*[Point(lat, lon) for lat, lon in s])

        trajectory_r = Trajectory(points_r, len_r)
        trajectory_s = Trajectory(points_s, len_s)

        return self.lib.distance(
            ctypes.byref(trajectory_r),
            ctypes.byref(trajectory_s),
            sigma
        )
