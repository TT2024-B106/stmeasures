import pytest
from stmeasures.calculate.euclidean import Euclidean

@pytest.fixture(scope="module")
def euclidean():
    instance = Euclidean()

    assert instance.lib is not None

    return instance

def test_basic(euclidean):
    approx_val = 2.8284271247461903
    assert euclidean.distance([1, 2], [3, 4]) == pytest.approx(approx_val)
