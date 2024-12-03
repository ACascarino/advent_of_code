import advent_of_code_utils as aoc_utils


def app(puzzle_input: str) -> int:
    left, right = zip(*aoc_utils.input_split_int(puzzle_input))
    diffs = (abs(l - r) for l, r in zip(sorted(left), sorted(right)))
    return sum(diffs)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
