#!/usr/bin/python3

import numpy as np
cimport cython
from libc.math cimport sqrt
from libc.math cimport abs


@cython.boundscheck(False)
@cython.wraparound(False)
def DTWDistance(double[:] s1, double[:] s2):
    """ Computes the dtw between s1 and s2 with distance the absolute distance

    :param s1: the first serie (ie an iterable over floats64)
    :param s2: the second serie (ie an iterable over floats64)
    :returns: the dtw distance
    :rtype: float64
    """
    cdef int len_s1 = len(s1)
    cdef int len_s2 = len(s2)
    cdef double[:, :] _dtw_mat = np.empty([len_s1, len_s2])
    cdef int j
    cdef int i
    cdef  double dist
    _dtw_mat[0, 0] = abs(s1[0] - s2[0])

    #  two special cases : filling first row and columns

    for j in range(1, len_s2):
        dist = abs(s1[0]-s2[j])
        _dtw_mat[0, j] = dist + _dtw_mat[0, j-1]

    for i in range(1, len_s1):
        dist = abs(s1[i]-s2[0])
        _dtw_mat[i, 0] = dist + _dtw_mat[(i-1, 0)]

    # filling the matrix
    for i in range(1, len_s1):
        for j in range(1, len_s2):
            dist = abs(s1[i]-s2[j])
            _dtw_mat[(i, j)] = dist + min(_dtw_mat[i-1, j],
                                          _dtw_mat[i, j-1],
                                          _dtw_mat[i-1, j-1])

    return _dtw_mat[len_s1-1, len_s2-1]


@cython.boundscheck(False)
@cython.wraparound(False)
def cort(double[:] s1, double[:] s2):
    """ Computes the cort between serie one and two (assuming they have the same length)

    :param s1: the first serie (or any iterable over floats64)
    :param s2: the second serie (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    cdef int t
    cdef double num = 0.0
    cdef double sum_square_x = 0.0
    cdef double sum_square_y = 0.0
    cdef int len_s1 = len(s1)
    cdef double slope_1
    cdef double slope_2
    for t in range(len(s1)-1):
        slope_1 = s1[t+1] - s1[t]
        slope_2 = s2[t+1] - s2[t]
        num = num + slope_1 * slope_2
        sum_square_x = sum_square_x + (slope_1*slope_1)
        sum_square_y = sum_square_y + (slope_2 * slope_2)
    return num/(sqrt(sum_square_x*sum_square_y))
