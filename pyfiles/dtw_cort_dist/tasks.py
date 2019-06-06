from pathlib import Path
from invoke import task

here = Path(__file__).parent.absolute()

directories = sorted(here.glob("V*"))


@task
def clean(c):
    for path in directories:
        if (path / "Makefile").exists():
            c.run(f"cd {path} && make clean", echo=True)


@task
def build(c):
    for path in directories:
        if (path / "Makefile").exists():
            c.run(f"cd {path} && make", echo=True)


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
