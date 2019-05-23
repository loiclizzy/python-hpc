from setuptools import setup, Extension

version = '0.1'

module_distance = Extension(name="distances", sources=["cdtw.c"],
                              extra_compile_args=["-O3", "-mavx2"],
                              extra_link_args=["-O3"]
                              )

setup(name='timeseries',
      version=version,
      description="data scientist tool for time series",
      long_description="data scientist tool for time series",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='timeseries, classification, machine learning, big data, spark',
      author='IKATS project',
      author_email='Franck.Thollard@imag.fr',
      url='http://ikats.imag.fr',
      license='GPL',
      include_package_data=True,
      zip_safe=False,
      install_requires=["cffi", "numpy", "setuptools"],
      entry_points="",
      ext_modules=[module_distance],
      )
