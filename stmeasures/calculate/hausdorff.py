import ctypes

_libhausdorff_path = "libhausdorff.so"
_libhausdorff = ctypes.CDLL(_libhausdorff_path)

def hausdorff_distance(p: list[float], q: list[float]) -> float:
    len_p, len_q = len(p), len(q)

    if not p or not q:
        raise ValueError("One or both arrays are empty")

    doublearray = ctypes.c_double * len_p
    doublearray_q = ctypes.c_double * len_q

    _libhausdorff.hausdorff_distance.argtypes = [doublearray, doublearray_q, ctypes.c_size_t, ctypes.c_size_t]
    _libhausdorff.hausdorff_distance.restype = ctypes.c_double

    return _libhausdorff.hausdorff_distance(doublearray(*p), doublearray_q(*q), len_p, len_q)
