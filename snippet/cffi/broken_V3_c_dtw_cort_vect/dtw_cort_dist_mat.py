#!/usr/bin/env python

import os
import argparse
import numpy as np
from cffi import FFI
import sysconfig

ffi = FFI()
ffi.cdef("double dtw(double* x, double* y, int size_x, int size_y);")
my_dir = os.path.dirname(os.path.realpath(__file__))
dllib = ffi.dlopen(
    os.path.join(my_dir, "distances" + sysconfig.get_config_var("EXT_SUFFIX"))
)


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


def cDTW(serie_a, serie_b):
    a_ptr = ffi.cast("double*", serie_a.ctypes.data)
    b_ptr = ffi.cast("double*", serie_b.ctypes.data)
    ret = dllib.dtw(a_ptr, b_ptr, len(serie_a), len(serie_b))
    return ret


def cort(s1, s2):
    """ Computes the cort between serie one and two (assuming they have the same length)

    :param s1: the first serie (or any iterable over floats64)
    :param s2: the second serie (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    d1 = np.diff(s1)
    d2 = np.diff(s2)
    num = np.dot(d1, d2.T)
    norm1 = np.dot(d1, d1.T)
    norm2 = np.dot(d2, d2.T)
    if np.abs(norm1) < 0.00001:
        norm1 = 1.0
    if np.abs(norm2) < 0.00001:
        norm2 = 1.0
    return num / np.sqrt(norm1 * norm2)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="Computes the distance matrix btw series"
    )
    PARSER.add_argument(
        "input", type=str, help="input file ", nargs="?", default="../data.npy"
    )
    PARSER.add_argument(
        "-n", type=int, default=None, help="number of series (default all 200)"
    )
    PARSER.add_argument(
        "-v", action="store_true", default=None, help="visualize the matrix"
    )

    ARGS = PARSER.parse_args()

    series = None
    # load the input data
    series = np.load(ARGS.input)

    if ARGS.n:
        nb_series = ARGS.n
    else:
        nb_series = series.shape[0]

    from time import time

    t0 = time()

    gen = serie_pair_index_generator(nb_series)

    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros((nb_series, nb_series), dtype=np.float64)
    for t1, t2 in gen:
        dist_dtw = cDTW(series[t1], series[t2])
        _dist_mat_dtw[t1, t2] = dist_dtw
        _dist_mat_dtw[t2, t1] = dist_dtw
        dist_cort = 0.5 * (1 - cort(series[t1], series[t2]))
        _dist_mat_cort[t1, t2] = dist_cort
        _dist_mat_cort[t2, t1] = dist_cort

    print("\nelapsed time = {:.3f} s".format(time() - t0))

    if ARGS.v:
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2)
        cax0 = axes[0].imshow(_dist_mat_dtw, cmap=plt.cm.gray)
        axes[0].set_title("dtw")
        cax1 = axes[1].imshow(_dist_mat_cort, cmap=plt.cm.gray)
        axes[1].set_title("cort")
        plt.show()
