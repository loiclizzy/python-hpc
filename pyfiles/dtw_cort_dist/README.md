
## Timing:

We use [invoke](https://www.pyinvoke.org/) (`pip install invoke`) to build and run the benchmarks.

See [how to get autocompletion with invoke](http://docs.pyinvoke.org/en/1.2/invoke.html?highlight=completion#cmdoption-print-completion-script).

After `inv build`, you should get something like this:

```bash
inv bench
V1_numpy_loops/dtw_cort_dist_mat.py data.npy
elapsed time = 10.106 s
V2_c_dtw/dtw_cort_dist_mat.py data.npy
elapsed time = 1.782 s
V5_cython/dtw_cort_dist_mat.py data.npy
elapsed time = 0.149 s
V6_pythran/dtw_cort_dist_mat.py data.npy
elapsed time = 0.018 s
V7_numba/dtw_cort_dist_mat.py data.npy
elapsed time = 0.866 s
mpirun -np 2 V8_mpi4py/dtw_cort_dist_mat.py data.npy
elapsed time = 5.048 s
elapsed time = 5.048 s
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

For a longer benchmark:

```bash
inv bench --medium
V2_c_dtw/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 60.530 s
V5_cython/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 24.439 s
V6_pythran/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 24.511 s
V6_pythran_aot/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 24.563 s
V6_pythran_no_transonic/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 24.586 s
V7_numba/dtw_cort_dist_mat.py data_medium.npy
elapsed time = 36.549 s

```
