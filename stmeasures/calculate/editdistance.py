"""Edit Distance algorithm class."""

import ctypes

from stmeasures.calculate.base import BaseAlgorithm

class EditDistance(BaseAlgorithm):
    """An Edit Distance instance that computes edit distances between two
    trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, default: "libeditdist"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the Edit Distance with Real Penalty of Point 1 (1, 2) and
    Point 2 (3, 4)

    >>> editdistance = EditDistance() # Intializes object and loads shared library
    >>> editdistance.erp([1,2],[3,4])
    4.0
    """

    def __init__(self, libname="libeditdist") -> None:
        super().__init__(libname)

    def ers(
            self,
            r: list[float],
            s: list[float],
            sigma: float = 1.0,
            cost_deletion: float = 1.0,
            cost_insertion: float = 1.0,
            subcost_within_sigma: float = 0.0,
            subcost_outside_sigma: float = 1.0
        ) -> float:
        """Return the Edit Distance on Real Sequences (ERS).

        Parameters
        ----------
        r : list[float]
            A first vector in n-space.
        s : list[float]
            A second vector in n-space.
        sigma : float, default: 1.0
            A matching threshold (tolerance).
        cost_deletion : float, default: 1.0
            The cost of deleting an element to match the sequence.
        cost_insertion : float, default: 1.0
            The cost of adding an element to match the sequence.
        subcost_within_sigma : float, default: 0.0
            The subcost when the threshold is matched.
        subcost_outside_sigma : float, default: 1.0
            The subcost when the threshold is not matched.
        """
        len_r, len_s = len(r), len(s)

        # TODO: Validate in `validate` module

        r_array = ctypes.c_double * len_r
        s_array = ctypes.c_double * len_s

        self.lib.ers.argtypes = [
            r_array,
            s_array,
            ctypes.c_size_t,
            ctypes.c_size_t,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
        ]
        self.lib.ers.restype = ctypes.c_double

        return self.lib.ers(
            r_array(*r),
            s_array(*s),
            len_r,
            len_s,
            sigma,
            cost_deletion,
            cost_insertion,
            subcost_within_sigma,
            subcost_outside_sigma
        )

    def erp(
            self,
            r: list[float],
            s: list[float],
            g: float = 0.0
        ) -> float:
        """Return the Edit Distance with Real Penalty (ERP).

        Parameters
        ----------
        r : list[float]
            A first vector in n-space.
        s : list[float]
            A second vector in n-space.
        g : float, default: 0.0
            The gap constant of edit distance.
        """
        len_r, len_s = len(r), len(s)

        # TODO: Validate in `validate` module

        r_array = ctypes.c_double * len_r
        s_array = ctypes.c_double * len_s

        self.lib.erp.argtypes = [
            r_array,
            s_array,
            ctypes.c_size_t,
            ctypes.c_size_t,
            ctypes.c_double,
        ]
        self.lib.erp.restype = ctypes.c_double

        return self.lib.erp(
            r_array(*r),
            s_array(*s),
            len_r,
            len_s,
            g
        )
