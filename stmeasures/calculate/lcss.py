"""LCSS algorithm class."""

import ctypes

from stmeasures.calculate.base import BaseAlgorithm

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

    def distance(
            self,
            r: list[float],
            s: list[float],
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

        r_array = ctypes.c_double * len_r
        s_array = ctypes.c_double * len_s

        self.lib.distance.argtypes = [
            r_array,
            s_array,
            ctypes.c_size_t,
            ctypes.c_size_t,
            ctypes.c_double,
        ]
        self.lib.distance.restype = ctypes.c_double

        return self.lib.distance(
            r_array(*r),
            s_array(*s),
            len_r,
            len_s,
            sigma
        )
