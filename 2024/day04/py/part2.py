import advent_of_code_utils as aoc_utils
import re

MAS_COUTERPARTS = {"S.S": "M.M", "S.M": "S.M", "M.S": "M.S", "M.M": "S.S"}


def check_xmas(grid: list[str]) -> int:
    return sum(line.count("XMAS") + line.count("SAMX") for line in grid)


def rot90_strings(mat: list[str]) -> list[str]:
    return list("".join(list(x)) for x in zip(*mat))[::-1]


def rot45_strings(mat: list[str]) -> list[str]:
    # We assume here that mat is square
    m = n = len(mat[0])
    return [
        "".join([mat[i][j] for j in range(n) for i in range(m) if i + j == layer])
        for layer in range(2 * n - 1)
    ]


def app(puzzle_input: str) -> int:
    lines = puzzle_input.splitlines()
    for lno, line in enumerate(lines):
        matches = re.finditer(r"(?=((S|M).(S|M)))", line)
        results = [(match.start(), match.group(1)) for match in matches]
        print(lno, *results)


if __name__ == "__main__":
    solution = app(aoc_utils.get_test())
    aoc_utils.say(solution)
