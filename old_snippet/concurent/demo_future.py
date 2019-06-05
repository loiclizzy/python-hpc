#!/usr/bin/env python

import concurrent.futures as futures
import itertools
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def profile(func):
    """ decorator that profile a function """
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return wrapper


def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    logging.debug("starting factorize_naive({})".format(n))
    if n < 2:
        logging.debug("ending factorize_naive({}) = []".format(n))
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            logging.debug("ending factorize_naive({}) = {}".format(n, factors))
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            logging.debug("ending factorize_naive({}) = {}".format(n, factors))
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1


def run_func(func, nb_jobs, inputs):
    """run fib in // for  each element of the iterable
    :param func: (callale) function to call. Take as input one parameter
    :param nb_jobs: (int) the number of jobs to run in parallel
    :param inputs: iterable over parameters
    :return: (dic) key is the input, value is the value returned by the func
    """
    # We can use a with statement to ensure threads are cleaned up promptly
    future_to_data = {}
    with futures.ProcessPoolExecutor(max_workers=nb_jobs) as executor:
        future_to_data = {executor.submit(func, data): data for data in inputs}
        # all the future object has been submitted -> they are running
        # iteration over dictionary iterates over keys
    logging.debug("end of submit")
    """
    for f in future_to_data:
        data = future_to_data[f]
        yield data, f.result()
    """
    for f in futures.as_completed(future_to_data):
        data = future_to_data[f]
        yield data, f.result()


def main():
    """run main
    """
    inputs = itertools.chain(range(100), range(200000, 12000000, 100))
    # logging.info("len inputs=%d", len(inputs))
    for data, res in run_func(factorize_naive, 4, inputs):
        logging.info("f({}) = {}".format(data, res))


if __name__ == "__main__":
    main()
