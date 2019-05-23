#!/usr/bin/env python3

from functools import partial
from runpy import run_path
from pathlib import Path

import numpy as np

from dtw_cort import cort, DTWDistance

print("util = {}".format(Path(__file__).parent.parent))

util = run_path(Path(__file__).parent.parent / "util.py")

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


def compute(series, nb_series):
    gen = serie_pair_index_generator(nb_series)
    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros((nb_series, nb_series), dtype=np.float64)
    for t1, t2 in gen:
        dist_dtw = DTWDistance(series[t1], series[t2])
        _dist_mat_dtw[t1, t2] = dist_dtw
        _dist_mat_dtw[t2, t1] = dist_dtw
        dist_cort = 0.5 * (1 - cort(series[t1], series[t2]))
        _dist_mat_cort[t1, t2] = dist_cort
        _dist_mat_cort[t2, t1] = dist_cort

    return _dist_mat_dtw, _dist_mat_cort


main = partial(util["main"], compute)


if __name__ == "__main__":

    main()
