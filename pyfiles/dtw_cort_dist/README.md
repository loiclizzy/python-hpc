Slides are available in
profile_python.svg
which can be visualize using a web browser
and navigated through the arrows keys

#### commands for profiling

`time ./dtw_cort_dist_mat.py`

`python3 -m cProfile -s cumulative -o profile_data.pyprof dtw_cort_dist_mat.py`

`pyprof2calltree -i profile_data.pyprof -k`

#### compiling library using setup.py

see the setup.py file (in particular things related to the ext_modules:

ext_modules=[module_distance]

then

`python3 setup.py build_ext`

will compile your lib.

##### NOTE:

the lib has to be found by your program. On linux (at least), this means that
the lib must be in a classical lib path or that the LD_LIBRARY_PATH is set
correctly.

##### Note2:

More on profiling in the stackoverflow discussion:

https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script

Timing:

```bash
for d in V*; do echo -n "$d"; $d/dtw_cort_dist_mat.py; done
V1_numpy_loops
elapsed time = 10.221 s
V2_c_dtw
elapsed time = 1.808 s
V5_cython
elapsed time = 0.146 s
V6_pythran
elapsed time = 0.018 s
V7_numba
elapsed time = 0.862 s
```

Note that using Pythran speedups the computations by a factor larger than 500
(!) compared to the (very bad) solutions with numpy loops. With Transonic, it
is as easy as adding 2 lines in the code:

```bash
diff V1_numpy_loops/dtw_cort_dist_mat.py V6_pythran/dtw_cort_dist_mat.py
8a9,10
> from transonic import jit
>
82a85
> @jit
```
