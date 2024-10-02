import ctypes

from stmeasures import _libpath

class BaseAlgorithm():
    def __init__(self, libname: str) -> None:
        self._libpath = _libpath(libname)
        self._lib = None

        self._load_library()

    @property
    def lib(self) -> ctypes.CDLL:
        if hasattr(self, '_lib') and type(self._lib) == ctypes.CDLL:
            return self._lib
        else:
            raise RuntimeError(
                f"Shared library '{self._libpath}' is not loaded"
            )

    def _load_library(self) -> None:
        try:
            self._lib = ctypes.CDLL(self._libpath)
        except OSError as ose:
            raise RuntimeError(
                f"Failed to load the shared library '{self._libpath}':\n"
                + f"{ose}"
            )
        except Exception as e:
            raise RuntimeError(
                f"An unexpected error occurred while loading '{self._libpath}'"
                + f":\n{e}"
            )
