import os
import ctypes

_libfilename = "libeuclidean.so"
_libpath = os.path.join(os.path.dirname(__file__), _libfilename)
_lib = ctypes.CDLL(_libpath)

def distance(p: list[float], q: list[float]) -> float:
    len_p, len_q = len(p), len(q)

    if not p or not q:
        raise ValueError("One or both arrays are empty")
    if len_p != len_q:
        raise ValueError(f"Arrays are not the same size\n{p}\n{q}")

    doublearray = ctypes.c_double * len_p
    _lib.distance.argtypes = [doublearray, doublearray, ctypes.c_size_t]
    _lib.distance.restype = ctypes.c_double

    return _lib.distance(doublearray(*p), doublearray(*q), len_p)
