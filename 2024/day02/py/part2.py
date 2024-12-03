import itertools
import pathlib
import statistics


def say(x):
    print("\n", x)


def cmp(a: int, b: int):
    return int(a > b) - int(a < b)


def safe(report: list[int]):
    diffs = (abs(a - b) for a, b in itertools.pairwise(report))
    cmps = sum(cmp(a, b) for a, b in itertools.pairwise(report))
    return all(1 <= x <= 3 for x in diffs) and (abs(cmps) == len(report) - 1)


def dampened_safe(report: list[int]):
    made_safe = False
    unsafe_index = None
    diffs = [abs(a - b) for a, b in itertools.pairwise(report)]
    diffs_safe = [1 <= x <= 3 for x in diffs]
    cmps = [cmp(a, b) for a, b in itertools.pairwise(report)]

    if not (abs(sum(cmps)) == len(cmps)):  # i.e. cmps unsafe
        desired_dir = statistics.mode(cmps)
        unsafe_index = [i for i, x in enumerate(cmps) if x != desired_dir][0]
    elif sum(diffs_safe) == len(diffs) - 1:  # i.e. one diff is unsafe
        unsafe_index = [i for i, x in enumerate(diffs_safe) if not x][0]

    if unsafe_index is not None:
        a = report[:]
        del a[unsafe_index]
        if safe(a):
            made_safe = True
        else:
            b = report[:]
            del b[unsafe_index + 1]
            if safe(b):
                made_safe = True
    return made_safe


def app(input_path: pathlib.Path):
    with open(input_path, "rt") as f:
        input = f.read()
    reports = (
        [int(level) for level in line.strip().split()] for line in input.splitlines()
    )

    return sum(safe(report) or dampened_safe(report) for report in reports)


if __name__ == "__main__":
    here = pathlib.Path(__file__).absolute()
    result = app(here.parent.parent / "input.txt")
    say(result)
