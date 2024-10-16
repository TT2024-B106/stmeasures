# frechet.py
import ctypes
import os
from stmeasures.calculate.base import BaseAlgorithm

class Frechet(BaseAlgorithm):
    def __init__(self):
        """
        Initialize the Frechet algorithm class. This loads the shared C library (libfrechet.so)
        and defines the argument and return types for the frechet_distance function.
        """
        super().__init__()
        
        # Path to the shared library (libfrechet.so)
        lib_name = "libfrechet.so"
        lib_path = os.path.join(os.path.dirname(__file__), '..', '..', lib_name)
        
        # Load the shared library using ctypes
        self.lib = ctypes.CDLL(lib_path)
        
        # Define the argument and return types for the frechet_distance C function
        self.lib.frechet_distance.argtypes = [
            ctypes.POINTER(ctypes.c_double), ctypes.c_size_t,
            ctypes.POINTER(ctypes.c_double), ctypes.c_size_t
        ]
        self.lib.frechet_distance.restype = ctypes.c_double

    def distance(self, curve1, curve2):
        """
        Calculate the Frechet distance between two curves.

        Args:
            curve1 (list of float): The first curve as a list of points [x1, y1, x2, y2, ...].
            curve2 (list of float): The second curve as a list of points [x1, y1, x2, y2, ...].

        Returns:
            float: The Frechet distance between the two curves.
        """
        # Get the number of points in each curve (assuming 2D points)
        size1 = len(curve1) // 2
        size2 = len(curve2) // 2
        
        # Convert the Python lists to C arrays
        array_type1 = ctypes.c_double * len(curve1)
        array_type2 = ctypes.c_double * len(curve2)
        c_curve1 = array_type1(*curve1)
        c_curve2 = array_type2(*curve2)
        
        # Call the C function frechet_distance and return the result
        return self.lib.frechet_distance(c_curve1, size1, c_curve2, size2)
