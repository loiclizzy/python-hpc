from pathlib import Path
import sys

this_dir = Path(__file__).parent

ipynb_files = tuple(this_dir.glob("*.ipynb"))

lines = [[] for day in range(4)]

for path in ipynb_files:
    name = path.with_suffix("").name
    day = int(name[0])
    text = name[3:].capitalize().replace("_", " ")
    path_html = name + ".slides.html"
    lines[day].append(f"- `{text} <{path_html}>`_")

back = "\n"

code = """
Python for HPC training UGA 2019
================================
"""

for iday, lines_day in enumerate(lines):
    lines_day.sort()
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