#!/usr/bin/python3

import multiprocessing as mp
import sys
import numpy as np

def is_prime(number):
    """return True if number is prime, else False

    :number: (int) a positive number (no check)
    :returns: (bool) true if number is prime, False else
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def first_primes(nb_to_check, nb_proc=None):
    """Prints the first prime numbers

    :bound: (int) number of primes to check
    :nb_proc: (int) the number of parallel jobs to run (default nb procs available)
    :returns: a list of the first nb_to_check prime numbers
    """
    inputs = range(2, nb_to_check)
    with mp.Pool(nb_proc) as pool:
        res = [False, False] + pool.map(is_prime, inputs)
        return [idx for (idx, e) in enumerate(res) if e]

def main(argv):
    if len(sys.argv) < 2:
        print(f"usage: {argv[0]} nb_prime_to_check [nb_procs=4]")
        sys.exit(1)
    if len(sys.argv) < 3:
        nb_proc = mp.cpu_count()
    else:
        nb_proc = int(sys.argv[2])
    nb_to_check = int(sys.argv[1])
    print(f"looking for the {nb_to_check} primes number using {nb_proc} procs")
    primes = first_primes(nb_to_check)
    print(f"first {nb_to_check} primes: {primes}")

if __name__ == '__main__':
    main(sys.argv)
