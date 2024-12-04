import advent_of_code_utils as aoc_utils


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

    # Need to check 8 directions. Set up the 3 other grids required for that.
    sideways_lines = rot90_strings(lines)
    diag_lines = rot45_strings(lines)
    other_diag_lines = rot45_strings(sideways_lines)

    return (
        check_xmas(lines)
        + check_xmas(sideways_lines)
        + check_xmas(diag_lines)
        + check_xmas(other_diag_lines)
    )


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
