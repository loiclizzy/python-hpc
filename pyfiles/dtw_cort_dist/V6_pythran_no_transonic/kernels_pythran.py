import numpy as np


def serie_pair_index_generator(number):
    " generator for pair index (i, j) such that i < j < number\n\n    :param number: the upper bound\n    :returns: pairs (lower, greater)\n    :rtype: a generator\n    "
    return (
        (_idx_greater, _idx_lower)
        for _idx_greater in range(number)
        for _idx_lower in range(_idx_greater)
    )


def DTWDistance(s1, s2):
    " Computes the dtw between s1 and s2 with distance the absolute distance\n\n    :param s1: the first serie (ie an iterable over floats64)\n    :param s2: the second serie (ie an iterable over floats64)\n    :returns: the dtw distance\n    :rtype: float64\n    "
    len_s1 = len(s1)
    len_s2 = len(s2)
    _dtw_mat = np.empty([len_s1, len_s2])
    _dtw_mat[(0, 0)] = abs((s1[0] - s2[0]))
    #  two special cases : filling first row and columns
    for j in range(1, len_s2):
        dist = abs((s1[0] - s2[j]))
        _dtw_mat[(0, j)] = dist + _dtw_mat[(0, (j - 1))]
    for i in range(1, len_s1):
        dist = abs((s1[i] - s2[0]))
        _dtw_mat[(i, 0)] = dist + _dtw_mat[((i - 1), 0)]
    #  filling the matrix
    for i in range(1, len_s1):
        for j in range(1, len_s2):
            dist = abs((s1[i] - s2[j]))
            _dtw_mat[(i, j)] = dist + min(
                _dtw_mat[((i - 1), j)],
                _dtw_mat[(i, (j - 1))],
                _dtw_mat[((i - 1), (j - 1))],
            )
    return _dtw_mat[((len_s1 - 1), (len_s2 - 1))]


def cort(s1, s2):
    """ Computes the cort between series one and two (assuming they have the same length)

    :param s1: the first series (or any iterable over floats64)
    :param s2: the second series (or any iterable over floats64)
    :returns: the cort distance
    :rtype: float64

    """
    slope_1 = s1[1:] - s1[:-1]
    slope_2 = s2[1:] - s2[:-1]
    num = np.sum(slope_1 * slope_2)
    sum_square_x = np.sum(slope_1 * slope_1)
    sum_square_y = np.sum(slope_2 * slope_2)
    return num / (np.sqrt(sum_square_x * sum_square_y))


# pythran export compute(float64[:, :], int)
def compute(series, nb_series):
    gen = serie_pair_index_generator(nb_series)
    _dist_mat_dtw = np.zeros((nb_series, nb_series), dtype=np.float64)
    _dist_mat_cort = np.zeros((nb_series, nb_series), dtype=np.float64)
    for (t1, t2) in gen:
        dist_dtw = DTWDistance(series[t1], series[t2])
        _dist_mat_dtw[(t1, t2)] = dist_dtw
        _dist_mat_dtw[(t2, t1)] = dist_dtw
        dist_cort = 0.5 * (1 - cort(series[t1], series[t2]))
        _dist_mat_cort[(t1, t2)] = dist_cort
        _dist_mat_cort[(t2, t1)] = dist_cort
    return (_dist_mat_dtw, _dist_mat_cort)
