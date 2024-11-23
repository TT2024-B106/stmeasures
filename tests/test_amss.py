from pytest import fixture
from pytest import approx

from stmeasures.calculate.amss import AMSS

@fixture(scope="module")
def amss():
    return AMSS()

def test_lib(amss):
    assert amss.lib is not None

def test_amss(amss):
    r = [(1, 2), (3, 4)]
    s = [(3, 4), (4, 5)]

    assert amss.distance(r, s) == approx(3.9667639723739727)
