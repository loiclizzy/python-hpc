Slides are available in
profile_python.svg
which can be visualize using a web browser
and navigated through the arrows keys

#### commands for profiling

`time ./dtw_cort_dist_mat.py ../data.npy`

`python3 -m cProfile -s cumulative -o profile_data.pyprof dtw_cort_dist_mat.py ../data.npy`

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

More on profiling on the stackoverflow discussion:

https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script

Basic timing:

```bash
for d in V*; do echo -n "$d"; cd $d; time python3 dtw_cort_dist_mat.py ../data.npy; cd ..; done
V1_pure_python
real 7,170	user 7,159	sys 0,008	pcpu 99,95

V2_c_dtw
real 1,395	user 1,369	sys 0,024	pcpu 99,88

V3_c_dtw_cort_vect
real 1,387	user 1,366	sys 0,020	pcpu 99,98

V4_c_dtw_c_cort
real 1,226	user 1,202	sys 0,024	pcpu 100,00

V5_cython
real 0,229	user 0,212	sys 0,016	pcpu 99,97

```

Timing computation:

```
for d in V*; do echo -n "$d"; $d/dtw_cort_dist_mat.py; done
V1_pure_python
elapsed time = 10.314 s
V2_c_dtw
elapsed time = 1.923 s
V5_cython
elapsed time = 0.155 s
V6_pythran
elapsed time = 0.021 s
V7_pythran_slow
elapsed time = 1.323 s
V8_numba
elapsed time = 0.947 s
```