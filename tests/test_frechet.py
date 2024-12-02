from pytest import fixture
from pytest import approx

from stmeasures.calculate.frechet import Frechet

@fixture(scope="module")
def frechet():
    return Frechet()

def test_lib(frechet):
    assert frechet.lib is not None

def test_basic(frechet):
    assert frechet.distance([(1, 0), (3, 5), (4, 2)], [(2, 1), (5, 4), (6, 3)]) == approx(2.23606797749979)

