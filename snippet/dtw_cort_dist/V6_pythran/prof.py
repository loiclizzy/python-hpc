
import cProfile
import pstats

from time import time

from dtw_cort_dist_mat import main, compute

series, nb_series = main(only_init=True)

t0 = t0 = time()
a, b = compute(series, nb_series)
t_end = time()
print('\nelapsed time = {:.3f} s'.format(t_end - t0))

t0 = t0 = time()
cProfile.runctx("a, b = compute(series, nb_series)", globals(), locals(), "prof.pstats")
t_end = time()


s = pstats.Stats('prof.pstats')
s.sort_stats('time').print_stats(12)


print('\nelapsed time = {:.3f} s'.format(t_end - t0))

print(
    '\nwith gprof2dot and graphviz (command dot):\n'
    'gprof2dot -f pstats prof.pstats | dot -Tpng -o prof.png')
