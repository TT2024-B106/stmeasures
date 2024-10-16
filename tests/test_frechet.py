import pytest

from stmeasures.calculate.frechet import Frechet

@pytest.fixture(scope="module")
def frechet():
    return Frechet()

def test_lib(frechet):
    assert frechet.lib is not None

def test_basic(frechet):
    assert frechet.distance([1, 2], [3, 4]) == approx(4.0)
