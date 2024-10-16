from pytest import fixture
from pytest import approx

from stmeasures.calculate.editdistance import EditDistance

@fixture(scope="module")
def editdistance():
    return EditDistance()

def test_lib(editdistance):
    assert editdistance.lib is not None

def test_erp(editdistance):
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = [2, 2, 2, 2, 5, 6, 7, 8, 9, 10]

    assert editdistance.erp(r, s) == approx(4.0)
