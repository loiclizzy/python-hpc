"""

  Module for computing distances between timeseries.
  Available distances includes cort, dtw, dtw_cort.
  It requires numpy.

"""

import numpy as np
from cffi import FFI
import platform

def load_shared():
    """
    Loads a wrapper over the shared library). The shared library is built
    using the command line python3 setup.py build_ext
    The library path should include the path where the shared library is.

    """

    ffi = FFI()
    ffi.cdef("""
    double dtw(double* x, double* y, int start_x, int start_y, int end_x, int end_y, int nbvar);
    int get_idx(int var_idx, int time_idx, int nbvar);
    double compute_diff(double *x, double *y, int t_x, int t_y, int nbvar);
    void compute_slope(double *x, int start_x, int end_x, int nb_var, double *res);
    void swap_pointers(double **x, double **y);
    void print_multivariate(double *x, int nbvar, int timelen);
    double dtw_cort_multivariate_no_path(double* x, double* y, int start_x, int start_y, int end_x, int end_y, int nbvar, double k);
    double cort(double *x, double *y, const unsigned time_start, const unsigned time_end,  const unsigned nb_var);
    """)
    if platform.system() == 'Linux':
        _lib_name =  "distances.cpython-34m.so"
    elif platform.system() == 'Darwin':
        _lib_name = "distances.cpython-35m-darwin.so"
    else:
        raise RuntimeError("unhandled system {}, cannot load dynamic library".format(platform.system()))
    return (ffi, ffi.dlopen(_lib_name))



def dtw(serie_a, serie_b, interval_a=None, interval_b=None, shared_lib=None):
    """ Computes the dynamic time wrapping distance between (multivariate )serie_a and serie_b.

    :param serie_a: the first serie
    :type serie_a: timeseries.TimeSeries
    :param serie_b: the second serie
    :type serie_b: timeseries.TimeSeries
    :param interval_a: time interval considered for serie_a (whole interval if None). Default=None.
    :type interval_a: a tuple that represents the interval (start included, end excluded)
    :param interval_b: time interval considered for serie_b (whole interval if None). Default=None.
    :type interval_b: a tuple that represents the interval (start included, end excluded)
    :param shared_lib:  the ffi wrapping over the shared lib (as returned by load_shared()). \
     Default value is shared lib is loaded.
    :type shared_lib: (ffi, dllib)

    :note: The local difference between two points of the time serie is the sum of the absolute \
           differences of the variables.

    """
    if shared_lib is None:
        (ffi, dllib) = load_shared()
    else:
        (ffi, dllib) = shared_lib
    a_ptr = ffi.cast("double*", serie_a.data().ctypes.data)
    b_ptr = ffi.cast("double*", serie_b.data().ctypes.data)
    time_start_a = 0 if interval_a is None else interval_a[0]
    time_end_a = serie_a.time_len() if interval_a is None else interval_a[1]
    time_start_b = 0 if interval_b is None else interval_b[0]
    time_end_b = serie_b.time_len() if interval_b is None else interval_b[1]
    return dllib.dtw(a_ptr, b_ptr, time_start_a, time_start_b, time_end_a, time_end_b,
                     serie_a.nb_variables())


