# Training Python HPC at UGA

This repository contains documents for a course on using Python for High
Performance Computing.

Although this is not classic for an interpreted language, we will see that we
can take advantage of many Python features to go toward high performances.

Before considering performances, we will address the problem of evaluating
performance, a.k.a. profiling Python code.



## Format et dates

sur 2 semaines

- 2 jours contigus (intro / numpy / matplot / pandas)
- 1 jour doc et package
- 2 jours contigus calcul intensif et optimisation

#### Dates sessions

- 12-13/06/2019 et 17-19/06/2019

## Prerequisites

- Coding experience with Python (see [UGA Python
  training](https://gricad-gitlab.univ-grenoble-alpes.fr/python-uga/py-training-2017))

- Algorithmics (loops, conditions)

- Knowledge of basic Linux command-line instructions (`ls`, `cd`)

## Planning

- Introduction, rappels langage Python et gestion de src [1j : 12/06] (Pierre,
Raphaël et Loïc)

- Numpy [0,5j : 13/06] (Loïc et Raphaël)

  _reprendre le contenu de l'initiation + vectorisation_

  - fancy indexing, masking
  - broadcast
  - vectorisation (vectoriser un pb ex : distance euclidienne en calcul matriciel)

- Visualisation - Matplotlib and other tools [0,25j : 13/06] (Loïc et Raphaël)

  - matplotlib orienté object (axes, features...) Loïc
  - figures et animations Loïc
  - voir graph plotting python jackc (Raphaël)
  - point bokeh, plotly, seaborn (Raphaël)

- Pandas [0,25j : 13/06] (Eric - Raphaël)
  - load, query, display, export

- Packaging et documentation [0,5j : 17/06] (Raphaël et Pierre)

  ex : fluidsim et autres

- wrapping low level code and/or compiled code [0,5j : 17/06] (Franck et Loic)

  - présentation du running example (pour wrap/calcul intensif et optimisation)
  - cffi (for external compiled C code)
  - f2py (to call fortran code from Python)
  - swig (to wrap external code -- like C, C++, Fortran -- and call it from Python)
  - pybind11 (C++)

- Calcul intensif et optimisation [2j : 18/06 et 19/06]

  - Profiling (Pierre et Franck)
    - cprofile (pstat...)
    - kcachegrind
    - Memory (see HPC book oreilly)

  - Different ways to speed up native Python code (Pierre - Franck)
    - using on the fly compiler (like e.g. numba)
    - using static compilers (like e.g. pythran)
    - using cython (évocation juste)

  - Tools for parallelisation (e.g. threading / multiprocessing / futures / openmp / mpi4py / GPU / joblib / dask ) (Pierre - Franck)

  - Déploiement sur cluster et mésocentre (lien singularity, charlie cloud) (Franck - Raphaël)

Exemples tranversaux (wrapping, optimisation...)

### Présence formateurs

- m: matin
- a: après-midi

|         | m 12 | a 12 | m 13 | a 13 | m 17 | a 17 | m 18 | a 18 | m 19 | a 19 |
|---------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Eric    |      |      |      |  x   |      |      |      |      |      |      |
| Franck  |      |      |      |      |      |  x   |  x   |  x   |  x   |  x   |
| Loïc    |      |      |  x   |  x   |      |  x   |      |      |      |      |
| Raphaël |  x   |   x  |  x   |  x   |  x   |      |      |      |      |  x   |
| Pierre  |  x   |   x  |      |      |  x   |      |  x   |  x   |  x   |      |
| Cyrille |      |      |      |      |      |      |      |      |      |      |

## To be done before the first day of the training session

We will have to use Python 3 (with Miniconda3), a good Python IDE (either
Spyder or VSCode), Jupyter and a version-control tool (Mercurial, or Git if you
know it and really like it).

We give indications about how to install these tools and how to get the
repository of this training locally on your computer. Please, try to do this
before the training and tell us if you encounter problems. You can fill an
issue
[here](https://gricad-gitlab.univ-grenoble-alpes.fr/python-uga/training-hpc/issues)
to explain what you did and what are the errors (please copy / paste the error
log).


#### Install Python and utilities

The first steps are to install miniconda3 (see
[here](https://docs.conda.io/en/latest/miniconda.html)) and VSCode (see
[here](https://code.visualstudio.com/download)).

On Windows, all commands have to be run in the conda prompt.

You will need to activate the conda channel `conda-forge` with:

```conda config --add channels conda-forge```

With miniconda, it should be simple to install Spyder and Jupyter either with the
command `conda install spyder jupyter` or using the graphical tool [Anaconda
Navigator](https://docs.anaconda.com/anaconda/navigator/).

To install and setup Mercurial, you can follow the instructions
[here](https://fluiddyn.readthedocs.io/en/latest/mercurial_bitbucket.html).

Warning: Mercurial **has to be correctly setup**! Since we will use [the Gitlab
instance of UGA](https://gricad-gitlab.univ-grenoble-alpes.fr), the Mercurial
extension hg-git has to be activated so the line `hggit =` in the configuration
file is mandatory.


#### Clone this repository

Once everything is installed and setup, you should be able to clone the
repository of the training with:

```hg clone https://gricad-gitlab.univ-grenoble-alpes.fr/python-uga/training-hpc.git```

Please tell us before the training if it does not work.

#### Install few packages in your base conda environment

```
conda install ipython spyder jupyter numpy scipy pandas matplotlib
```

#### Check your environment

Once the repository is cloned you should have a new directory `training-hpc`
and you should be able to enter into it with `cd training-hpc`.

Finally, you can check that your Python environment is all fine with:

```python check_env.py```
