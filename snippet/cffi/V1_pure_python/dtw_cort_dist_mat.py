#!/usr/bin/python3 -OO


import argparse
import numpy as np

def serie_pair_index_generator(number):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    return ((_idx_greater, _idx_lower) for _idx_greater in range(number)
            for _idx_lower in range(number) if _idx_lower < _idx_greater)

def DTWDistance(s1, s2):
    """ Computes the dtw between s1 and s2 with distance the absolute distance

    :param s1: the first serie (ie an iterable over floats64)
    :param s2: the second serie (ie an iterable over floats64)
    :returns: the dtw distance
    :rtype: float64
    """
    _dtw_mat={}

    for i in range(len(s1)):
        _dtw_mat[(i, -1)] = float('inf')
    for i in range(len(s2)):
        _dtw_mat[(-1, i)] = float('inf')
    _dtw_mat[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= abs(s1[i]-s2[j])
            _dtw_mat[(i, j)] = dist + min(_dtw_mat[(i-1, j)],_dtw_mat[(i, j-1)], _dtw_mat[(i-1, j-1)])

    return _dtw_mat[len(s1)-1, len(s2)-1]

def cort(s1, s2):
    """ Computes the cort between serie one and two (assuming they have the same length)

    :param s1: the first serie (or any iterable over floats64)
    :param s2: the second serie (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    sum = 0.0
    num = 0.0
    sum_square_x = 0.0
    sum_square_y = 0.0
    for t in range(len(s1)-1):
        slope_1 = s1[t+1] - s1[t]
        slope_2 = s2[t+1] - s2[t]
        num += slope_1 * slope_2
        sum_square_x += slope_1*slope_1
        sum_square_y += slope_2 * slope_2
    return num/(np.sqrt(sum_square_x*sum_square_y))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Computes the distance matrix btw series")
    PARSER.add_argument("input", type=str, help="input file ")
    PARSER.add_argument("-n", type=int, default=None, help="number of series (default all 200)")
    PARSER.add_argument("-v", action="store_true", default=None, help="visualize the matrix")

    ARGS = PARSER.parse_args()

    series = None
    # load the input data
    series = np.load(ARGS.input)

    if ARGS.n:
        nb_series = ARGS.n
    else:
        nb_series = series.shape[0]
    gen = serie_pair_index_generator(nb_series)
    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros((nb_series, nb_series), dtype=np.float64)
    for t1, t2 in gen:
        dist_dtw = DTWDistance(series[t1], series[t2])
        _dist_mat_dtw[t1, t2] = dist_dtw
        _dist_mat_dtw[t2, t1] = dist_dtw
        dist_cort = 0.5*(1-cort(series[t1], series[t2]))
        _dist_mat_cort[t1, t2] = dist_cort
        _dist_mat_cort[t2, t1] = dist_cort


    if ARGS.v:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2)
        cax0 = axes[0].imshow(_dist_mat_dtw, cmap=plt.cm.gray)
        axes[0].set_title("dtw")
        cax1 = axes[1].imshow(_dist_mat_cort, cmap=plt.cm.gray)
        axes[1].set_title("cort")
        plt.show()
