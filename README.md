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

- Numpy / Scipy [0.5j : 13/06] (Loïc et Raphaël)

  - fancy indexing, masking
  - presentation of the example "dtw_cort_dist"
  - broadcast
  - vectorizing

- Visualization - Matplotlib and other tools [0.25j : 13/06] (Loïc et Raphaël)

  - matplotlib object oriented (axes, features...) (Loïc)
  - figures et animations (Loïc)
  - voir graph plotting python jackc (Raphaël)
  - point bokeh, plotly, seaborn (Raphaël)

- Pandas [0.25j : 13/06] (Eric - Raphaël)
  - load, query, display, export

- Packaging, documentation and testing [0.5j : 17/06] (Raphaël et Pierre)

- General introduction HPC with Python [0.25j] (Pierre)

- Profiling [0.25j] (Pierre et Franck)

  See the book "High performance Python".

  - perf
  - cprofile (pstat, SnakeViz)
  - pyperf
  - line_profiler
  - kcachegrind
  - Memory (memory_profiler, ...)

- Wrapping low level code and/or compiled code [0.5j] (Franck et Loic)

  Mainly for legacy code...

  ctypes, cffi, cython, cppyy, pybind11, f2py, pyo3, swig

- Different ways to speed up native Python code [0.5j] (Pierre - Franck)

  - using on the fly compiler (like e.g. numba)
  - using static compilers (like e.g. pythran)
  - using cython (évocation juste)
  - transonic

- Tools for parallelisation [0.25j]

  threading / multiprocessing / concurrent.futures / OpenMP / mpi4py / GPU /joblib / dask (Pierre - Franck)

- Déploiement sur cluster et mésocentre (lien singularity, charlie cloud) [0.25j] (Franck - Raphaël)

- Travaux sur projets personnels [0.5j au moins]


### Présence formateurs

- m: matin
- a: après-midi

|         | m 12 | a 12 | m 13 | a 13 | m 17 | a 17 | m 18 | a 18 | m 19 | a 19 |
|---------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Eric    | (x)  | (x)  | (x)  | (x)  | (x)  |      | (x)  | (x)  | (x)  | (x)  |
| Franck  |      |      |      |      |      |  x   |  x   |  x   |  x   |  x   |
| Loïc    |      |      |  x   |  x   |      |  x   |      |      |      |      |
| Raphaël |  x   |   x  |  x   |  x   |  x   |      |      |      |      |  x   |
| Pierre  |  x   |   x  |      |      |  x   |  x   | (x)  |  x   |  x   | (x)  |
| Cyrille |      |      |      |      |      |      |      |      |      |      |

## To be done before the first day of the training session

We will have to use Python 3 (with Miniconda3), a good Python IDE (either
Spyder or VSCode), Jupyter and a version-control tool (Mercurial, or Git if you
know it and really like it).

In the following, we give indications about how to install these tools and how
to get the repository of this training locally on your computer. Please, try to
do this before the training and tell us if you encounter problems. You can fill
an issue
[here](https://gricad-gitlab.univ-grenoble-alpes.fr/python-uga/training-hpc/issues)
to explain what you did and what are the errors (please copy / paste the error
log).

Moreover, let's add that the best OS for HPC (and HPC with Python) is
Linux/GNU. Windows (at least without
[WLS](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)) and even
macOS are less adapted for this particular application. Python is a
cross-platform language but nevertheless, you will get a better experience for
HPC with Python on Linux. Therefore, we encourage the participant to work
during this training with a (real or
[virtual](https://www.virtualbox.org/wiki/Downloads)) Linux machine. Of course,
if you can't or don't want to use Linux, come with your computer on Windows or
macOS.
We offer a linux virtual machine ready to use (via virtualbox 6.X) for training.
It can be downloaded [here](https://filesender.renater.fr/?s=download&token=62c5f530-7def-8c32-4e3c-d205299a5201)


#### Install Python and utilities

The first steps are to install miniconda3 (see
[here](https://docs.conda.io/en/latest/miniconda.html)) and VSCode (see
[here](https://code.visualstudio.com/download)).

On Windows, all commands have to be run in the conda prompt.

You will need to activate the conda channel `conda-forge` with:

```conda config --add channels conda-forge```

With miniconda, it should be simple to install Spyder and Jupyter either with
the command `conda install spyder jupyterlab` or using the graphical tool
[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).

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

#### Build the presentations

One needs Jupyter, rst2html5 (installable with `pip install rst2html5`), plus
`make` and few other Unix tools. Therefore, it is not easy to build the website
on Windows.

On Unix-like systems, `make presentations` should build the presentations and
`make serve` should start a server to visualize them in a browser.
