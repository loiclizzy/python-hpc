import argparse
from time import time
from pathlib import Path

import numpy as np

path_data = Path(__file__).parent / "data.npy"


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


def main(compute, only_init=False):

    parser = argparse.ArgumentParser(
        description="Computes the distance matrix btw series"
    )
    parser.add_argument(
        "input", type=str, help="input file ", nargs="?", default=path_data
    )
    parser.add_argument(
        "-n", type=int, default=None, help="number of series (default all 200)"
    )
    parser.add_argument(
        "-s", type=str, default=None, help="save the matrices (provide prefixes)"
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

    if only_init:
        return series, nb_series

    t0 = time()
    _dist_mat_dtw, _dist_mat_cort = compute(series, nb_series)
    print("elapsed time = {:.3f} s".format(time() - t0))

    if args.s:
        dtw_mat = "{}_dtw".format(args.s)
        np.save(dtw_mat, _dist_mat_dtw)
        cort_mat = "{}_cort".format(args.s)
        np.save(cort_mat, _dist_mat_cort)

    if args.v:
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2)
        axes[0].imshow(_dist_mat_dtw, cmap=plt.cm.gray)
        axes[0].set_title("dtw")
        axes[1].imshow(_dist_mat_cort, cmap=plt.cm.gray)
        axes[1].set_title("cort")
        plt.show()
