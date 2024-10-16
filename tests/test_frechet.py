import pytest
from stmeasures.calculate.frechet import Frechet

@pytest.fixture(scope="module")
def frechet():
    return Frechet()

def test_lib(frechet):
    assert frechet.lib is not None

def test_frechet_basic(frechet):
    approx_val = 2.8284271247461903  # Adjust this based on your expected value
    assert frechet.distance([1, 1, 2, 2], [3, 3, 4, 4]) == pytest.approx(approx_val)
