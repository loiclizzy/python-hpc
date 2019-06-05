from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['dtw_cort.pyx'],
                          annotate=True),
)
