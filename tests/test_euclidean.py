from stmeasures.calculate import euclidean

def test_basic():
    assert euclidean.distance([1, 2], [3, 4]) == 2.8284271247461903
