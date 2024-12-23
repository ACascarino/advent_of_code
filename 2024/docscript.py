from pathlib import Path

here = Path(".")
for day in range(1, 26):
    newdir = here / f"day{day:02}"
    newdir.mkdir(parents=True, exist_ok=True)
for child in here.rglob("**/day*"):
    newpydir = child / "py"
    newpydir.mkdir(parents=True, exist_ok=True)
    with (child / "input.txt").open("a") as file:
        file.write("")
    with (child / "test.txt").open("a") as file:
        file.write("")
    with (newpydir / "part1.py").open("a") as file:
        file.write("")
    with (newpydir / "part2.py").open("a") as file:
        file.write("")
