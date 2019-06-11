from pathlib import Path
from invoke import task
import numpy as np

here = Path(__file__).parent.absolute()

directories = sorted(here.glob("V*"))


@task
def clean(c):
    for path in directories:
        if (path / "Makefile").exists():
            c.run(f"cd {path} && make clean", echo=True)
            for algo in ("dtw", "cort"):
                f = path / "ref_{algo}.npy"
                if f.exists():
                    f.unlink()

@task
def build(c):
    for path in directories:
        if (path / "Makefile").exists():
            c.run(f"cd {path} && make", echo=True)

@task
def check(c):
    ref_dtw = np.load("ref_small_dtw.npy")
    ref_cort = np.load("ref_small_cort.npy")

    for path in directories:
        c.run(f"cd {path} && ./dtw_cort_dist_mat.py -s res", echo=True)
        calc_dtw = np.load(f"{path / 'res_dtw.npy'}")
        print(f"{path.name} dtw : allclose {np.allclose(ref_dtw, calc_dtw)}")
        calc_cort = np.load(f"{path / 'res_cort.npy'}")
        print(f"{path.name} cort: allclose {np.allclose(ref_cort, calc_cort)}")


@task
def bench(c, medium=False):
    if medium:
        datafile = "data_medium.npy"
    else:
        datafile = "data.npy"
    for path in directories:
        if medium and ('numpy' in str(path) or "mpi4py" in str(path)):
            continue
        path = path.relative_to(here)
        command = f"{path / 'dtw_cort_dist_mat.py'} {datafile}"
        if 'mpi4py' in str(path):
            command = "mpirun -np 2 " + command
        c.run(command, echo=True)
