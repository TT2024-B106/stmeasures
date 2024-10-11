from ..stmeasures.calculate import hausdorff

def test_basic():
    assert hausdorff.hausdorff_distance([1, 2, 3], [4, 5, 6]) == 3.0
