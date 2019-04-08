#!/usr/bin/python3

import multiprocessing as mp
import sys
import numpy as np

def closer(item, collection, dist):
    """Look for the element in collection  that is the closest to number.
       Basic algorithm : iterate over collection and compute dist
       Complexity = O(|collection| * O(dist))

    :item: an element to look for
    :collection: (iterable) collection of elements that are comparable with item
    :dist: function that takes two items and return the distance between them
    :returns: item of the collection that is the closest to item.

    """
    closest, distance = min(((e, dist(item, e)) for e in collection),
                            key=lambda x: x[0])
    return closest


def abs_dist(x, y):
    """return the absolute of the difference of the inputs """
    return abs(x-y)


def main(argv):
    if len(sys.argv) < 2:
        print(f"usage: {argv[0]} [nb_procs=4]")
        sys.exit(1)

    dist_mat = None
    col = np.random.random(1000)
    items = np.random.random(100)
    inputs = [(x, col, abs_dist) for x in items]
    with mp.Pool(5) as pool:
        dist_mat = pool.starmap(closer, inputs)
    for idx, elem in enumerate(dist_mat):
        print(f'closest to {col[idx]} -> {elem}')

if __name__ == '__main__':
    main(sys.argv)
