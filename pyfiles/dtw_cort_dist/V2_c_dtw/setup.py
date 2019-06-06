from setuptools import setup, Extension

version = "0.1"

module_distance = Extension(
    name="cdtw",
    sources=["cdtw.c"],
    extra_compile_args=["-O3", "-mavx2"],
    extra_link_args=["-O3"],
)

setup(
    name="dtw_cort_dist_mat",
    version=version,
    description="data scientist tool for time series",
    long_description="data scientist tool for time series",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    author="IKATS project",
    author_email="Franck.Thollard@imag.fr",
    url="http://ikats.imag.fr",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    install_requires=["cffi", "numpy", "setuptools"],
    entry_points="",
    ext_modules=[module_distance],
)
