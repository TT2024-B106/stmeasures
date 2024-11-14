"""Calculate module for various distance algorithms."""

from typing import Dict as _Dict
from typing import Optional as _Optional

import stmeasures.calculate.rdp as _scrd
import stmeasures.calculate.dtw as _scdt
import stmeasures.calculate.lcss as _sclc
import stmeasures.calculate.frechet as _scfr
import stmeasures.calculate.hausdorff as _scha
import stmeasures.calculate.editdistance as _sced
import stmeasures.calculate.euclidean as _sceu
from stmeasures._algorithms import Algorithms

_rdp = _scrd.RDP()
_dtw = _scdt.DTW()
_lcss = _sclc.LCSS()
_frechet = _scfr.Frechet()
_hausdorff = _scha.Hausdorff()
_editdistance = _sced.EditDistance()
_euclidean = _sceu.Euclidean()

def simplify(trajectory, tolerance):
    """
    Simplify a trajectory using the Ramer-Douglas-Peucker algorithm.

    Parameters
    ----------
    trajectory : list[tuple[float, float]]
        The trajectory points to simplify.
    tolerance : float
        The tolerance value that determines the degree of simplification.

    Returns
    -------
    list[tuple[float, float]]
        A simplified version of the input trajectory.
    """
    return _rdp.simplify(trajectory, tolerance)

def distance(a, b, normalize=False):
    """
    Compute multiple distance metrics between trajectories.

    Parameters
    ----------
    a, b : list[tuple[float, float]]
        Trajectories to calculate the distance between.
    normalize : bool, optional
        Whether to normalize the results. Defaults to False.

    Returns
    -------
    float
        The computed distance if `normalize` is False, or the normalized
        minimum distance if True.
    """
    results: _Dict[str, float] = dict()

    results[Algorithms.EUCLIDEAN] = _euclidean.distance(a, b)

    if not normalize:
        return results[Algorithms.EUCLIDEAN]

    results[Algorithms.DTW] = _dtw.distance(a, b)
    results[Algorithms.LCSS] = _lcss.distance(a, b)
    results[Algorithms.FRECHET] = _frechet.distance(a, b)
    results[Algorithms.HAUSDORFF] = _hausdorff.distance(a, b)
    results[Algorithms.ERS] = _editdistance.ers(a, b)
    results[Algorithms.ERP] = _editdistance.erp(a, b)

    return min(-1, list(results.values()))  # TODO: normalize.all(results)

def distance_spatial(
        a: list[tuple[float, float]],
        b: list[tuple[float, float]],
        normalize=False,
        algorithm: _Optional[Algorithms] = None
    ) -> float:
    """
    Compute a spatial distance metric between trajectories.

    Parameters
    ----------
    a, b : list[tuple[float, float]]
        Trajectories to calculate the spatial distance between.
    normalize : bool, optional
        Whether to normalize the results. Defaults to False.
    algorithm : Algorithms, optional
        The algorithm to use for spatial distance. Defaults to Euclidean.

    Returns
    -------
    float
        The computed spatial distance, or the normalized minimum distance if
        requested.
    """
    results: _Dict[str, float] = dict()
    algorithm = algorithm or Algorithms.EUCLIDEAN

    if algorithm == Algorithms.EUCLIDEAN or normalize:
        results[Algorithms.EUCLIDEAN] = _euclidean.distance(a, b)
    if algorithm == Algorithms.HAUSDORFF or normalize:
        results[Algorithms.HAUSDORFF] = _hausdorff.distance(a, b)
    if algorithm == Algorithms.FRECHET or normalize:
        results[Algorithms.FRECHET] = _frechet.distance(a, b)
    if algorithm not in Algorithms.SPATIAL:
        raise ValueError(f"Spatial algorithm not supported: {algorithm}")

    if not normalize:
        return results[algorithm]

    return next(iter(list(results.values())))  # TODO: normalize.spatial(results)?

def distance_geometrical(
        a: list[tuple[float, float]],
        b: list[tuple[float, float]],
        normalize=False,
        algorithm: _Optional[Algorithms] = None
    ) -> float:
    """
    Compute a geometrical distance metric between trajectories.

    Parameters
    ----------
    a, b : list[tuple[float, float]]
        Trajectories to calculate the geometrical distance between.
    normalize : bool, optional
        Whether to normalize the results. Defaults to False.
    algorithm : Algorithms, optional
        The algorithm to use for geometrical distance. Defaults to Hausdorff.

    Returns
    -------
    float
        The computed geometrical distance, or the normalized minimum distance
        if requested.
    """
    results: _Dict[str, float] = dict()
    algorithm = algorithm or Algorithms.HAUSDORFF

    if algorithm == Algorithms.HAUSDORFF or normalize:
        results[Algorithms.HAUSDORFF] = _hausdorff.distance(a, b)
    if algorithm == Algorithms.FRECHET:
        results[Algorithms.FRECHET] = _frechet.distance(a, b)
    if algorithm not in Algorithms.GEOMETRICAL:
        raise ValueError(f"Geometrical algorithm not supported: {algorithm}")

    if not normalize:
        return results[algorithm]

    return next(iter(list(results.values())))  # TODO: normalize.geometrical(results)?

def distance_temporal(
        a: list[tuple[float, float]],
        b: list[tuple[float, float]],
        normalize=False,
        algorithm: _Optional[Algorithms] = None,
        *args
    ) -> float:
    """
    Compute a temporal distance metric between trajectories.

    Parameters
    ----------
    a, b : list[tuple[float, float]]
        Trajectories to calculate the temporal distance between.
    normalize : bool, optional
        Whether to normalize the results. Defaults to False.
    algorithm : Algorithms, optional
        The algorithm to use for temporal distance. Defaults to DTW.
    *args : tuple
        Additional arguments for certain algorithms (e.g., ERP, ERS).

    Returns
    -------
    float
        The computed temporal distance, or the normalized minimum distance if
        requested.
    """
    results: _Dict[str, float] = dict()
    algorithm = algorithm or Algorithms.DTW

    if algorithm == Algorithms.DTW or normalize:
        results[Algorithms.DTW] = _dtw.distance(a, b)
    if algorithm == Algorithms.ERP or normalize:
        results[Algorithms.ERP] = _editdistance.erp(a, b, *args)
    if algorithm == Algorithms.ERS or normalize:
        results[Algorithms.ERS] = _editdistance.ers(a, b, *args)
    if algorithm == Algorithms.LCSS or normalize:
        results[Algorithms.ERP] = _lcss.distance(a, b, *args)
    if algorithm not in Algorithms.TEMPORAL:
        raise ValueError(f"Temporal algorithm not supported: {algorithm}")

    if not normalize:
        return results[algorithm]

    return next(iter(list(results.values())))  # TODO: normalize.temporal(results)?

def distance_sequential(
        a: list[tuple[float, float]],
        b: list[tuple[float, float]],
        normalize=False,
        algorithm: _Optional[Algorithms] = None,
        *args
    ) -> float:
    """
    Compute a sequential distance metric between trajectories.

    Parameters
    ----------
    a, b : list[tuple[float, float]]
        Trajectories to calculate the sequential distance between.
    normalize : bool, optional
        Whether to normalize the results. Defaults to False.
    algorithm : Algorithms, optional
        The algorithm to use for sequential distance. Defaults to ERP.
    *args : tuple
        Additional arguments for certain algorithms (e.g., ERP, ERS).

    Returns
    -------
    float
        The computed sequential distance, or the normalized minimum distance
        if requested.
    """
    results: _Dict[str, float] = dict()
    algorithm = algorithm or Algorithms.ERP

    if algorithm == Algorithms.ERP:
        results[Algorithms.ERP] = _editdistance.erp(a, b, *args)
    if algorithm == Algorithms.ERS:
        results[Algorithms.ERS] = _editdistance.ers(a, b, *args)
    if algorithm == Algorithms.LCSS:
        results[Algorithms.LCSS] = _lcss.distance(a, b, *args)
    if algorithm not in Algorithms.SEQUENTIAL:
        raise ValueError(f"Sequential algorithm not supported: {algorithm}")

    if not normalize:
        return results[algorithm]

    return next(iter(list(results.values())))  # TODO: normalize.sequential(results)?
