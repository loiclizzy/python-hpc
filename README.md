This project provides a course on using python for High Performance Computing. 

Although this is not classical for a interpreted language, we will see that we 
can take advantage of many python features to go toward high performances. 

Before considering performances, we will adress the problem of evaluating 
performance, a.k.a. adressing the problem of profiling python code. 


Among them, we will adress here:

- tools for parallelisation (e.g. the threading / multiprocessing / futures / 
  mpi4py modules)
- different ways to speed up native python code:
  * using cython
  * using on the fly compiler (like e.g. numba)
  * using static compilers (like e.g. pythrans)
  
- wrapping low level code and/or compiled code:
  * cffi (for external compiled C code)
  * f2py (to call fortran code from python)
  * swig (to wrap external code -- like C, C++, Fortranc -- and call it from python)
  
  
