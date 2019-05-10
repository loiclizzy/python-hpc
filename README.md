# Training Python HPC at UGA

This repository contains documents for a course on using Python for High
Performance Computing.

Although this is not classic for an interpreted language, we will see that we
can take advantage of many python features to go toward high performances.

Before considering performances, we will address the problem of evaluating
performance, a.k.a. profiling python code.

## Format

sur 2 semaines

- 2 jours contigus (intro / numpy / matplot / pandas)
- 1 jour doc et package
- 2 jours contigus calcul intensif et optimisation

## Dates 1st session

12-13/06/2019 and 17-19/06/2019

## TODO

- étoffer les contenus!!
- ...

## Pré-requis

- expérience de code avec python (voir formation python initiation UGA)
- algo (boucles, conditions)
- connaissances des commandes de bases linux (ls, cd, voir formation CED)

### Pré-requis technique

- conda
- spyder et vscode
- mercurial et git

First, install miniconda3 (see
[here](https://docs.conda.io/en/latest/miniconda.html)) and vscode.

To install Mercurial, you can follow the instructions
[here](https://fluiddyn.readthedocs.io/en/latest/mercurial_bitbucket.html).

## A planning projection

- Introduction, rappels langage python, gestion de src (1j) (Pierre - Raphael/Loic) 12/06

- Numpy (0,5j) (LOIC - Raphael) 13/06 reprendre le contenu de l'initiation + vectorisation

  - fancy indexing, masking
  - broadcast
  - vectorisation (vectoriser un pb ex : distance euclidienne en calcul matriciel)

- Visualisation - Matplotlib et autres outils à évoquer (0,25j) (LOIC -Raphael) 13/06

  - matplotlib orienté object (axes, features...) Loic
  - figures et animations Loic
  - voir graph plotting python jackc (raphael)
  - point bokeh, plotly, seaborn (raphael)

- Pandas (0,25j) (Eric - Raphaël) 13/06

  - load, query, display, export

- Documentation et package (0,5j) (Raphaël - Pierre) ex : fluidsim et autres 17/06

- wrapping low level code and/or compiled code  (Franck - Loic) (0,5j) 17/06

  - présentation du running example (pour wrap/calcul intensif et optimisation)
  - cffi (for external compiled C code)
  - f2py (to call fortran code from python)
  - swig (to wrap external code -- like C, C++, Fortran -- and call it from python)
  - pybind11 (C++)

- Calcul intensif et optimisation (2j) 18/06 19/06
  - Profiling  (Pierre - Franck) (0,5)
    - cprofile (pstat...)
    - kcachegrind
    - Memory (see HPC book oreilly)

  - different ways to speed up native python code (Pierre - Franck) (0,5)
    - using on the fly compiler (like e.g. numba)
    - using static compilers (like e.g. pythran)
    - using cython (évocation juste)

  - tools for parallelisation (e.g. the threading / multiprocessing / futures / openmp / mpi4py / GPU / joblib / dask ) (Pierre - Franck)(0,5)

  - Déploiement sur cluster et mésocentre (lien singularity, charlie cloud) (Franck - Raphaël) (0,5)

Exemples tranversaux (wrapping, optimisation...)

### Présence formateurs

- m: matin
- a: après-midi

|         | m 12 | a 12 | m 13 | a 13 | m 17 | a 17 | m 18 | a 18 | m 19 | a 19 |
|---------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Eric    |      |      |      |  x   |      |      |      |      |      |      |
| Franck  |      |      |      |      |      |  x   |  x   |  x   |  x   |  x   |
| Loic    |      |      |  x   |  x   |      |  x   |      |      |      |      |
| Raphaël |  x   |   x  |  x   |  x   |  x   |      |      |      |      |  x   |
| Pierre  |  x   |   x  |      |      |  x   |      |  x   |  x   |  x   |      |
| Cyrille |      |      |      |      |      |      |      |      |      |      |