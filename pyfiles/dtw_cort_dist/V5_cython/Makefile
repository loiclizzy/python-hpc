
dtw_cort.so: setup.py dtw_cort.pyx
	python3 setup.py build_ext
	mv build/lib.linux-x86_64-3.7/dtw_cort.cpython-37m-x86_64-linux-gnu.so dtw_cort.so

run: dtw_cort.so
	python3 dtw_cort_dist_mat.py ../data.npy -s dists_cython.npz

test: dtw_cort.so
	python3 dtw_cort_dist_mat.py ../data.npy -s dists_cython.npz
	python3 check.py

clean:
	rm -rf build dtw_cort.c dtw_cort.so
	rm -f dists_cython.npz
	rm -f dtw_cort.html
