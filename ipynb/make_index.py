from pathlib import Path
import sys

titles = {
    "About": "About this training",
    "Intro first steps": "First step with Python",
    "Intro language": "Some characteristics of the language",
    "Readwritefiles": "Read and write files",
    "Import standard library": "Import statements and the standart library",
    "Data struct": "Standard data structure (list, tuple, set and dict)",
    "Oop encapsulation": "Object-oriented programming - encapsulation",
    "Oop inheritance": "Object-oriented programming - inheritance",
    "Intro hpc": "Introduction HPC with Python",
    "Packaging": "Packaging, documentation and unittest",
    "Numpy scipy": "Numpy / Scipy",
    "Wrapping": "Wrapping compiled code",
    "Accelerators": "Tools to accelerate Python code",
    "Parallel": "Parallel computing (CPU bounded)",
}

this_dir = Path(__file__).parent

ipynb_files = sorted(tuple(this_dir.glob("*.ipynb")))

lines = [[] for day in range(5)]

for path in ipynb_files:
    name = path.with_suffix("").name
    index, title = name.split("_", 1)
    day = int(index[0])
    title = title.capitalize().replace("_", " ")

    if title in titles:
        title = titles[title]

    path_html = name + ".slides.html"
    lines[day].append(f"- [{index}] `{title} <{path_html}>`_")

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
