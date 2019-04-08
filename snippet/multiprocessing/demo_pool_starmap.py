#!/usr/bin/python3

import multiprocessing as mp
import sys
import numpy as np

def distances(item, collection, dist):
    """Return the set of distances between item  and elements of collection,
       using dist as distance measure
       Complexity = O(|collection| * O(dist))

    :item: an element to look for
    :collection: (iterable) collection of elements that are comparable with item
    :dist: function that takes two items and return the distance between them
    :returns:(list) distances between item and each elem of collection
    """
    return [dist(item, e) for e in collection]

def abs_dist(x, y):
    """return the absolute of the difference of the inputs """
    return abs(x-y)

def compute_abs_dist(col, nb_proc):
    """Computes the distance matrix between elements in collection

    :col: (iterable) the set of elements to consider.
    :nb_proc: the number of parallel jobs to run
    :returns: distance matrix
    """
    inputs = [(x, col, abs_dist) for x in col]
    collection_size = len(col)
    dist_mat = None
    with mp.Pool(nb_proc) as pool:
        dist_mat = pool.starmap(distances, inputs)
    # results gets back sorted in the same order as provided
    res = np.empty([collection_size, collection_size])
    for idx, elem in enumerate(dist_mat):
        res[idx,:] = elem
    return res

def main(argv):
    if len(sys.argv) < 2:
        print(f"usage: {argv[0]} collection_size [nb_procs]")
        sys.exit(1)
    if len(sys.argv) < 3:
        nb_proc = mp.cpu_count()
    else:
        nb_proc = int(sys.argv[2])
    collection_size = int(sys.argv[1])
    col = np.random.random(collection_size)
    print(f"collection: {col}")
    res = compute_abs_dist(col, nb_proc)
    print(f"res={res}")
    import matplotlib.pyplot as plt
    plt.imshow(res)
    plt.show()

if __name__ == '__main__':
    main(sys.argv)
