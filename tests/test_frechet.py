# tests/test_frechet.py
import pytest
from stmeasures.calculate.frechet import Frechet

@pytest.fixture(scope="module")
def frechet():
    return Frechet()

def test_lib(frechet):
    assert frechet.lib is not None

def test_basic_zero_distance(frechet):
    # Identical curves should have zero Frechet distance
    curve1 = [0, 0, 1, 1, 2, 2]
    curve2 = [0, 0, 1, 1, 2, 2]
    expected_distance = 0.0
    calculated_distance = frechet.distance(curve1, len(curve1) // 2, curve2, len(curve2) // 2)
    assert calculated_distance == pytest.approx(expected_distance)

def test_basic_non_zero_distance(frechet):
    # Different curves should have a non-zero Frechet distance
    curve1 = [0, 0, 1, 1, 2, 2]
    curve2 = [0, 0, 1, 2, 2, 3]
    expected_distance = 1.0  # This is an example; actual distance may vary based on implementation
    calculated_distance = frechet.distance(curve1, len(curve1) // 2, curve2, len(curve2) // 2)
    assert calculated_distance == pytest.approx(expected_distance, abs=1e-6)
