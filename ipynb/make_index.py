from pathlib import Path
import sys

titles = {
    "Intro hpc": "Introduction HPC",
    "Packaging": "Package and document your Python software",
    "Numpy scipy": "Numpy / Scipy",
}

this_dir = Path(__file__).parent

ipynb_files = sorted(tuple(this_dir.glob("*.ipynb")))

lines = [[] for day in range(5)]

for path in ipynb_files:
    name = path.with_suffix("").name
    day = int(name[0])
    title = name[3:].capitalize().replace("_", " ")

    if title in titles:
        title = titles[title]

    path_html = name + ".slides.html"
    lines[day].append(f"- `{title} <{path_html}>`_")

back = "\n"

code = """
Python for HPC training UGA 2019
================================
"""

for iday, lines_day in enumerate(lines):
    code += f"""
Day {iday}
-----

{back.join(lines_day)}
"""

path_rst = this_dir / "index.rst"

if path_rst.exists():

    with open(path_rst) as file:
        old_code = file.read()

    if code == old_code:
        sys.exit(0)

print(f"override {path_rst}")

with open(path_rst, "w") as file:
    file.write(code)
