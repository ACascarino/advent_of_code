import advent_of_code_utils as aoc_utils
import itertools


def cmp(a: int, b: int):
    return int(a > b) - int(a < b)


def safe(report: list[int]):
    diffs = (abs(a - b) for a, b in itertools.pairwise(report))
    cmps = sum(cmp(a, b) for a, b in itertools.pairwise(report))
    return all(1 <= x <= 3 for x in diffs) and (abs(cmps) == len(report) - 1)


def app(puzzle_input: str) -> int:
    reports = (
        [int(level) for level in line.strip().split()] for line in puzzle_input.splitlines()
    )

    return sum(safe(report) for report in reports)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
