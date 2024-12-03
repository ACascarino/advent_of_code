import itertools
import pathlib


def say(x):
    print("\n", x)


def cmp(a: int, b: int):
    return int(a > b) - int(a < b)


def safe(report: list[int]):
    diffs = (abs(a - b) for a, b in itertools.pairwise(report))
    cmps = sum(cmp(a, b) for a, b in itertools.pairwise(report))
    return all(1 <= x <= 3 for x in diffs) and (abs(cmps) == len(report) - 1)


def app(input_path: pathlib.Path):
    with open(input_path, "rt") as f:
        input = f.read()
    reports = (
        [int(level) for level in line.strip().split()] for line in input.splitlines()
    )

    return sum(safe(report) for report in reports)


if __name__ == "__main__":
    here = pathlib.Path(__file__).absolute()
    result = app(here.parent.parent / "input.txt")
    say(result)
