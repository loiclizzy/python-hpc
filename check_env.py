import sys

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

try:
    import conda
except ImportError:
    print(
        "Problem: the conda package not importable.\n"
        "Please run this script in the base conda environment"
    )
    sys.exit(1)
else:
    print("Good! conda package importable!")

try:
    import numpy, scipy, matplotlib, pandas
except ImportError:
    print(
        "Problem: numpy, scipy, matplotlib, pandas not importable\n"
        "Maybe run:\nconda install numpy scipy matplotlib pandas"
    )
else:
    print("Good! numpy, scipy, matplotlib, pandas importable!")
