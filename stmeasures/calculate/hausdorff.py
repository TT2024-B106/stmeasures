import ctypes
from stmeasures.calculate.base import BaseAlgorithm

class Hausdorff(BaseAlgorithm):
    """A Hausdorff instance that computes the Hausdorff distance
    between two trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, default: "libhausdorff"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the Hausdorff distance between Point 1 (1, 2) and Point 2 (3, 4)

    >>> hausdorff = Hausdorff()  # Initializes object and loads shared library
    >>> hausdorff.distance([1, 2], [3, 4])
    2.0
    """

    def __init__(self, libname="libhausdorff") -> None:
        """Initialize the Hausdorff instance and load the shared library."""
        super().__init__(libname)

    def distance(self, p: list[float], q: list[float]) -> float:
        """Return the Hausdorff distance between two trajectories.

        Parameters
        ----------
        p : list[float]
            A first vector in n-space
        q : list[float]
            A second vector in n-space
        """
        len_p = len(p)
        len_q = len(q)

        # TODO: Validate in `validate` module

        # Define the array types for `p` and `q`
        doublearray_p = ctypes.c_double * len_p
        doublearray_q = ctypes.c_double * len_q

        # Set argument and return types for the C function
        self.lib.hausdorff_distance.argtypes = [
            doublearray_p,  # Array of doubles for `p`
            doublearray_q,  # Array of doubles for `q`
            ctypes.c_size_t,  # Size of `p`
            ctypes.c_size_t   # Size of `q`
        ]
        self.lib.hausdorff_distance.restype = ctypes.c_double

        # Call the C function and return the result
        return self.lib.hausdorff_distance(
            doublearray_p(*p),
            doublearray_q(*q),
            len_p,
            len_q
        )
