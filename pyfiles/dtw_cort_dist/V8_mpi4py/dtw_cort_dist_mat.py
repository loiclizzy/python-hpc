#!/usr/bin/env python3

from functools import partial
from runpy import run_path
from pathlib import Path

import numpy as np

from mpi4py import MPI
from distances_fort import dtw_cort

util = run_path(Path(__file__).absolute().parent.parent / "util.py")


def serie_pair_index_generator(number, rank, size):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    assert rank < size
    start = rank * number // (size * 2)
    end_inf = min((number + 1) // 2, (rank + 1) * ((number + 1) // 2) // size)
    end_sup = min(number // 2, (rank + 1) * number // (size * 2))

    for range_ in (
        range(start, end_inf),
        range(number - 1 - start, number - 1 - end_sup, -1),
    ):
        for _idx_greater in range_:
            for _idx_lower in range(_idx_greater):
                yield _idx_greater, _idx_lower


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


def compute(series, nb_series):
    comm = MPI.COMM_WORLD
    gen = serie_pair_index_generator(nb_series, comm.rank, comm.size)
    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros_like(_dist_mat_dtw)
    for t1, t2 in gen:
        dist_dtw = DTWDistance(series[t1], series[t2])
        _dist_mat_dtw[t1, t2] = dist_dtw
        _dist_mat_dtw[t2, t1] = dist_dtw
        dist_cort = 0.5 * (1 - cort(series[t1], series[t2]))
        _dist_mat_cort[t1, t2] = dist_cort
        _dist_mat_cort[t2, t1] = dist_cort

    _dist_mat_dtw_global = np.zeros_like(_dist_mat_dtw)
    _dist_mat_cort_global = np.zeros_like(_dist_mat_dtw)
    comm.Reduce(
        [_dist_mat_cort, MPI.DOUBLE],
        [_dist_mat_cort_global, MPI.DOUBLE],
        op=MPI.SUM,
        root=0,
    )
    comm.Reduce(
        [_dist_mat_dtw, MPI.DOUBLE],
        [_dist_mat_dtw_global, MPI.DOUBLE],
        op=MPI.SUM,
        root=0,
    )
    return _dist_mat_dtw_global, _dist_mat_cort_global


main = partial(util["main"], compute)

if __name__ == "__main__":
    main()
