from ..stmeasures.calculate import frechet

def test_basic():
    assert frechet.frechet_distance([1, 2, 3], [4, 5, 6]) == 3.0
