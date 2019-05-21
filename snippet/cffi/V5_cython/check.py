
import numpy as np
a = np.load("dists_cython.npz")
dtws_cython = a["arr_0"]
cort_cython = a["arr_1"]
ref = np.load("../dist_ref.npz")
dtws_ref = ref["arr_0"]
cort_ref = ref["arr_1"]

print("all close dtw: {}".format(np.allclose(dtws_cython, dtws_ref)))
print("all close dtw: {}".format(np.allclose(cort_cython, cort_ref)))

