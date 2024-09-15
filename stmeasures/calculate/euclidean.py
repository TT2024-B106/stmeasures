import ctypes

_libeuclidean_path = "libeuclidean.so"
_libeuclidean = ctypes.CDLL(_libeuclidean_path)

def distance(p: list[float], q: list[float]) -> float:
    len_p, len_q = len(p), len(q)

    if not p or not q:
        raise ValueError("One or both arrays are empty")
    if len_p != len_q:
        raise ValueError(f"Arrays are not the same size\n{p}\n{q}")

    doublearray = ctypes.c_double * len_p
    _libeuclidean.distance.argtypes = [doublearray, doublearray, ctypes.c_size_t]
    _libeuclidean.distance.restype = ctypes.c_double

    return _libeuclidean.distance(doublearray(*p), doublearray(*q), len_p)
