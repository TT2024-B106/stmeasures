import ctypes
import warnings

#from stmeasures.validation import validate_frechet, validate_trajectory
from stmeasures.calculate.base import BaseAlgorithm
from stmeasures.objects.cstructures import Trajectory, Point

class Frechet(BaseAlgorithm):
    """A Frechet instance that computes the Frechet distance
    between two trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, default: "libfrechet"
        The file name of the compiled shared library.

    Examples
    --------
    Calculating the Frechet distance between Point 1 (1, 2) and Point 2 (3, 4)

    >>> frechet = Frechet()  # Initializes object and loads shared library
    >>> frechet.distance([1, 2], [3, 4])
    2.828
    """

    def __init__(self, libname="libfrechet") -> None:
        """Initialize the Frechet instance and load the shared library."""
        super().__init__(libname)

        self.lib.frechet_execute.argtypes = [ctypes.POINTER(Trajectory), ctypes.POINTER(Trajectory)]
        self.lib.frechet_execute.restype = ctypes.c_double

    def distance(
            self,
            p: list[tuple[float, float]],
            q: list[tuple[float, float]]
        ) -> float:
        """Calculate the Frechet distance between two trajectories.

        Parameters
        ----------
        seq1 : list of tuple of float
            The first sequence of (latitude, longitude) tuples.
        seq2 : list of tuple of float
            The second sequence of (latitude, longitude) tuples.

        Returns
        -------
        float
            The Frechet distance between the two trajectories.
        """
        warnings.warn('Args not validating')
        #  # Validate the input trajectories
        # if not validate_frechet(p, q):
        #     raise ValueError("Invalid trajectories provided for Frechet distance calculation.")


        # Convert the input lists to Trajectory objects
        seq1_points = (Point * len(p))(*[Point(lat, lon) for lat, lon in p])
        seq2_points = (Point * len(q))(*[Point(lat, lon) for lat, lon in q])

        p_c = Trajectory(seq1_points, len(p))
        q_c = Trajectory(seq2_points, len(q))

        return self.lib.frechet_execute(ctypes.byref(p_c), ctypes.byref(q_c))