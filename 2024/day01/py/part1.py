import advent_of_code_utils as aoc_utils


def app(puzzle_input: str) -> int:
    lines = (line.strip() for line in puzzle_input.splitlines())
    left, right = zip(*(line.split() for line in lines))
    diffs = (abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right)))
    return sum(diffs)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
