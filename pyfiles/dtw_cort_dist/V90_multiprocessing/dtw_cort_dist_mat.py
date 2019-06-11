#!/usr/bin/env python3

from functools import partial
from runpy import run_path
from pathlib import Path
from distances_fort import dtw_cort
import multiprocessing as mp

import numpy as np

util = run_path(Path(__file__).absolute().parent.parent / "util.py")


def serie_pair_index_generator(number):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    return (
        (_idx_greater, _idx_lower)
        for _idx_greater in range(number)
        for _idx_lower in range(number)
        if _idx_lower < _idx_greater
    )


def DTWDistance(s1, s2):
    """ Computes the dtw between s1 and s2 with distance the absolute distance

    :param s1: the first serie (ie an iterable over floats64)
    :param s2: the second serie (ie an iterable over floats64)
    :returns: the dtw distance
    :rtype: float64
    """
    dtw_result = dtw_cort.dtwdistance(s1, s2)
    return dtw_result


def cort(s1, s2):
    """ Computes the cort between serie one and two (assuming they have the same length)

    :param s1: the first serie (or any iterable over floats64)
    :param s2: the second serie (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    cort_result = dtw_cort.cort(s1, s2)
    return cort_result


def distances(series, idx_s1, idx_s2):
    """Computes the distances (dtw and cort) of series s1, and s2
        and puts result in res_mat_dtw and res_mat_cort

    :series: (np array) series
    :idx_s1:  index of first serie in series
    :idx_s2: index of second serie in series
    :result:  (tuple) idx_s1, idx_s2, dtw and cort between series[s1] and series[s2]
    """
    dist_dtw = DTWDistance(series[idx_s1], series[idx_s2])
    dist_cort = 0.5 * (1 - cort(series[idx_s1], series[idx_s2]))
    return idx_s1, idx_s2, dist_dtw, dist_cort


def compute(series, nb_series):
    gen = serie_pair_index_generator(nb_series)
    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros((nb_series, nb_series), dtype=np.float64)
    inputs = ((series, t1, t2) for t1, t2 in gen)
    res = None
    with mp.Pool(4) as pool:
        res = pool.starmap(distances, inputs)
    for idx_s1, idx_s2, dist_dtw, dist_cort in res:
        _dist_mat_dtw[idx_s1, idx_s2] = dist_dtw
        _dist_mat_dtw[idx_s2, idx_s1] = dist_dtw
        _dist_mat_cort[idx_s1, idx_s2] = dist_cort
        _dist_mat_cort[idx_s2, idx_s1] = dist_cort
    return _dist_mat_dtw, _dist_mat_cort


main = partial(util["main"], compute)

if __name__ == "__main__":
    main()
