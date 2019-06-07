#!/usr/bin/env python3

from functools import partial
from runpy import run_path
from pathlib import Path

from kernels_pythran import compute

util = run_path(Path(__file__).absolute().parent.parent / "util.py")

main = partial(util["main"], compute)

if __name__ == "__main__":
    main()
