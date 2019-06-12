
build: setup.py dtw_cort.pyx
	python3 setup.py develop

run:
	python3 dtw_cort_dist_mat.py ../data.npy -s dists_cython.npz

test:
	python3 dtw_cort_dist_mat.py ../data.npy -s dists_cython.npz
	python3 check.py

clean:
	rm -rf build dtw_cort.c dtw_cort.*.so
	rm -f dists_cython.npz
	rm -f dtw_cort.html
