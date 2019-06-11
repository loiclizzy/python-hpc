#!/usr/bin/python3

import numpy as np
import sysconfig
from functools import partial
from cffi import FFI
from runpy import run_path
from pathlib import Path

util = run_path(Path(__file__).absolute().parent.parent / "util.py")

ffi = FFI()
ffi.cdef("double dtw(double* x, double* y, int size_x, int size_y);")
ffi.cdef("double cort(double* x, double* y, int size_x);")
my_dir = Path(__file__).absolute().parent
dllib = ffi.dlopen(
    str(my_dir / ("cdtw" + sysconfig.get_config_var("EXT_SUFFIX")))
)


def serie_pair_index_generator(number):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    return ((_idx_greater, _idx_lower) for _idx_greater in range(number)
            for _idx_lower in range(number) if _idx_lower < _idx_greater)


def cDTW(serie_a, serie_b):
    a_ptr = ffi.cast("double*", serie_a.ctypes.data)
    b_ptr = ffi.cast("double*", serie_b.ctypes.data)
    ret = dllib.dtw(a_ptr, b_ptr, len(serie_a), len(serie_b))
    return ret


def cort(serie_a, serie_b):
    """ Computes the cort between serie one and two (assuming they have the same length)

    :param s1: the first serie (or any iterable over floats64)
    :param s2: the second serie (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    a_ptr = ffi.cast("double*", serie_a.ctypes.data)
    b_ptr = ffi.cast("double*", serie_b.ctypes.data)
    ret = dllib.cort(a_ptr, b_ptr, len(serie_a))
    return ret

def compute(series, nb_series):
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

    return _dist_mat_dtw, _dist_mat_cort


main = partial(util["main"], compute)

if __name__ == "__main__":
    main()
