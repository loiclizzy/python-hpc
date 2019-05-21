#!/usr/bin/python3


import argparse
import numpy as np
import dtw_cort


def serie_pair_index_generator(number):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    return ((_idx_greater, _idx_lower) for _idx_greater in range(number)
            for _idx_lower in range(number) if _idx_lower < _idx_greater)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Computes the distance matrix btw series")
    PARSER.add_argument("input", type=str, help="input file ")
    PARSER.add_argument("-n", type=int, default=None, help="number of series (default all 200)")
    PARSER.add_argument("-s", type=str, default=None, help="save distance matrices")
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
        dist_dtw = dtw_cort.DTWDistance(series[t1], series[t2])
        _dist_mat_dtw[t1, t2] = dist_dtw
        _dist_mat_dtw[t2, t1] = dist_dtw
        dist_cort = 0.5*(1-dtw_cort.cort(series[t1], series[t2]))
        _dist_mat_cort[t1, t2] = dist_cort
        _dist_mat_cort[t2, t1] = dist_cort

    if ARGS.s:
        np.savez(ARGS.s, _dist_mat_dtw, _dist_mat_cort)

    if ARGS.v:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2)
        cax0 = axes[0].imshow(_dist_mat_dtw, cmap=plt.cm.gray)
        axes[0].set_title("dtw")
        cax1 = axes[1].imshow(_dist_mat_cort, cmap=plt.cm.gray)
        axes[1].set_title("cort")
        plt.show()
