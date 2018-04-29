Slides are available in 
profile_python.svg
which can be visualize using a web browser 
and navigated through the arrows keys

#### commands for profiling
time dtw_cort_dist_mat.py ../data.npy
python3 -OO -m cProfile -s cumulative -o profile_data.pyprof dtw_cort_dist_mat.py ../data.npy
pyprof2calltree -i profile_data.pyprof -k

#### compiling library using setup.py
see the setup.py file (in particular things related to the ext_modules:
ext_modules=[module_distance]
then 
>> python3 setup.py build_ext
will compile your lib. 

NOTE: 
the lib has to be found by your program. On linux (at least), this means that 
the lib must be in a classical lib path or that the LD_LIBRARY_PATH is set 
correctly. 


