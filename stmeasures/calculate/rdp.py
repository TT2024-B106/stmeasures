import ctypes
from stmeasures.calculate.base import BaseAlgorithm
from coordinates import Point, CoordinateSequence

class RDP(BaseAlgorithm):
    """An RDP class that implements the Ramer-Douglas-Peucker (RDP) algorithm
    for simplifying a sequence of coordinates.
    """

    def __init__(self, libname="librdp") -> None:
        super().__init__(libname)

        self.lib.rdp_execute.argtypes = [ctypes.POINTER(CoordinateSequence), ctypes.c_double]
        self.lib.rdp_execute.restype = CoordinateSequence

    def simplify(self, sequence: list[tuple[float, float]], tolerance: float) -> list[tuple[float, float]]:
        """Simplifies a sequence of coordinates using the RDP algorithm.
        
        Args:
            sequence (list[tuple[float, float]]): The original sequence of coordinates.
            tolerance (float): The tolerance for simplification. Higher tolerance results in more simplification.
        
        Returns:
            list[tuple[float, float]]: The simplified sequence of coordinates.
        """
        seq_points = (Point * len(sequence))(*[Point(lat, lon) for lat, lon in sequence])

        seq_c = CoordinateSequence(seq_points, len(sequence))

        simplified_seq_c = self.lib.rdp_execute(ctypes.byref(seq_c), tolerance)

        simplified_sequence = [
            (simplified_seq_c.points[i].latitude, simplified_seq_c.points[i].longitude)
            for i in range(simplified_seq_c.size)
        ]

        return simplified_sequence

