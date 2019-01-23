Nb d'etp : 

Cible juin 

Format
- 2 jours contigus (intro / numpy / matplot / pandas)
- 1 jour doc et package
- 2 jours contigus calcul intensif et optimisation
sur 2 semaines

TODO
- faire l'archi du repository git
- trouver les dates
- étoffer les contenus
- 

Pré-requis
- expérience de code avec python (voir formation python initiation UGA) 
- algo (boucles, conditions)
- connaissances des commandes de bases linux (ls, cd, voir formation CED)

Pré-requis technique
- conda
- spyder et vscode
- git

A planning projection 

- Introduction, rappels langage python, gestion de src (1j) (Pierre )
- Numpy (0,5j) (LOIC - Raphael)
    - fancy indexing, masking
    - broadcast
    - vectorisation
- Visualisation - Matplotlib et autres outils à évoquer (0,25j) (LOIC - )
    - matplotlib orienté object (axes, features...)
    - figures et animations
    - voir graph plotting python jack
- Pandas (0,25j) (Eric - Raphaël)
    - load, query, display, export
- Documentation  et package (0,5j) (Raphaël - Pierre) ex : fluidsim et autres
- wrapping low level code and/or compiled code  (Franck - Cyrille) (0,5j)
        - cffi (for external compiled C code)
        - f2py (to call fortran code from python)
        - swig (to wrap external code -- like C, C++, Fortran -- and call it from python)
- Calcul intensif et optimisation (2j)
   - Profiling  ( Pierre - Franck) (0,5)
        - cprofile (pstat...)
        - kcachegrind
        - Memory (see HPC book oreilly)
   -  different ways to speed up native python code ( Pierre - Franck) (0,5)
       - using on the fly compiler (like e.g. numba)
       - using static compilers (like e.g. pythran)
       - using cython (évocation juste)
   - tools for parallelisation (e.g. the threading / multiprocessing / futures / openmp / mpi4py / GPU / joblib / dask ) ( Pierre - Franck)(0,5)
    - Déploiement sur cluster et mésocentre (lien singularity, charlie cloud) (Cyrille - Raphaël) (0,5)

Exemples traversaux (wrapping, optimisation...)
Reprendre l'architecture notebook / make de la formation initiation...



This project provides a course on using python for High Performance Computing. 

Although this is not classical for a interpreted language, we will see that we 
can take advantage of many python features to go toward high performances. 

Before considering performances, we will adress the problem of evaluating 
performance, a.k.a. adressing the problem of profiling python code. 


Among them, we will adress here: