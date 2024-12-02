import ctypes
import warnings

#from stmeasures.validation import validate_hausdorff, validate_trajectory
from stmeasures.calculate.base import BaseAlgorithm
from stmeasures.objects.cstructures import Trajectory, Point

class Hausdorff(BaseAlgorithm):
    """A Hausdorff instance that computes the Hausdorff distance
    between two trajectories-like (`list[float]`).

    Parameters
    ----------
    libname : str, optional
        The file name of the compiled shared library. Defaults to "libhausdorff".

    Examples
    --------
    Calculating the Hausdorff distance between Point 1 (1, 2) and Point 2 (3, 4)

    >>> hausdorff = Hausdorff()  # Initializes object and loads shared library
    >>> hausdorff.distance([(1, 2)], [(3, 4)])
    314.395
    """

    def __init__(self, libname="libhausdorff") -> None:
        """Initialize the Hausdorff instance and load the shared library."""
        super().__init__(libname)

        self.lib.hausdorff_execute.argtypes = [ctypes.POINTER(Trajectory), ctypes.POINTER(Trajectory)]
        self.lib.hausdorff_execute.restype = ctypes.c_double


    def distance(
            self,
            p: list[tuple[float, float]],
            q: list[tuple[float, float]]
        ) -> float:
        """Calculate the Hausdorff distance between two trajectories.

        Parameters
        ----------
        p : list of tuple of float
            The first sequence of (latitude, longitude) tuples.
        q : list of tuple of float
            The second sequence of (latitude, longitude) tuples.

        Returns
        -------
        float
            The Hausdorff distance between the two trajectories.
         """
        warnings.warn('Args not validating')
        # # Validate the input trajectories
        # if not validate_trajectory(p) or not validate_trajectory(q):
        #     raise ValueError("Invalid trajectories provided for Hausdorff distance calculation.")
        
        # Convert the input lists to Trajectory objects
        seq1_points = (Point * len(p))(*[Point(lat, lon) for lat, lon in p])
        seq2_points = (Point * len(q))(*[Point(lat, lon) for lat, lon in q])

        p_c = Trajectory(seq1_points, len(p))
        q_c = Trajectory(seq2_points, len(q))

        return self.lib.hausdorff_execute(ctypes.byref(p_c), ctypes.byref(q_c))