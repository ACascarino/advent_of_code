from pathlib import Path

here = Path(".")
for child in here.rglob("**/day*"):
    newpydir = child / "py"
    newcppdir = child / "cpp"
    newpydir.mkdir(parents=True, exist_ok=True)
    newcppdir.mkdir(parents=True, exist_ok=True)

    with (newpydir / "part1.py").open("w") as file:
        file.write("")
    with (newpydir / "part2.py").open("w") as file:
        file.write("")
    with (newcppdir / "part1.cpp").open("w") as file:
        file.write("")
    with (newcppdir / "part2.cpp").open("w") as file:
        file.write("")
