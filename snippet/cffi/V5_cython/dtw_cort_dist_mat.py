#!/usr/bin/env python

import argparse
import numpy as np
from dtw_cort import cort, DTWDistance


def serie_pair_index_generator(number):
    """ generator for pair index (i, j) such that i < j < number

    :param number: the upper bound
    :returns: pairs (lower, greater)
    :rtype: a generator
    """
    return ((_idx_greater, _idx_lower) for _idx_greater in range(number)
            for _idx_lower in range(number) if _idx_lower < _idx_greater)


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


def main():

    parser = argparse.ArgumentParser(
        description="Computes the distance matrix btw series"
    )
    parser.add_argument(
        "input", type=str, help="input file ", nargs="?", default="../data.npy"
    )
    parser.add_argument(
        "-n", type=int, default=None, help="number of series (default all 200)"
    )
    parser.add_argument(
        "-v", action="store_true", default=None, help="visualize the matrix"
    )

    args = parser.parse_args()

    series = None
    # load the input data
    series = np.load(args.input)

    if args.n:
        nb_series = args.n
    else:
        nb_series = series.shape[0]

    from time import time

    t0 = time()
    _dist_mat_dtw, _dist_mat_cort = compute(series, nb_series)
    print("\nelapsed time = {:.3f} s".format(time() - t0))

    if args.v:
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2)
        cax0 = axes[0].imshow(_dist_mat_dtw, cmap=plt.cm.gray)
        axes[0].set_title("dtw")
        cax1 = axes[1].imshow(_dist_mat_cort, cmap=plt.cm.gray)
        axes[1].set_title("cort")
        plt.show()


if __name__ == "__main__":

    main()
