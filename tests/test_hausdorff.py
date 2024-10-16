import pytest

from stmeasures.calculate.hausdorff import Hausdorff

@pytest.@fixture(scope="module")
def hausdorff():
    return Hausdorff()

def test_lib(hausdorff):
    assert hausdorff.lib is not None

def test_basic(hausdorff):
    assert hausdorff.distance([1, 2], [3, 4]) == approx(4.0)
