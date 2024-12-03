import advent_of_code_utils as aoc_utils
import collections


def app(puzzle_input: str) -> int:
    left, right = zip(*aoc_utils.input_split_int(puzzle_input))
    r_counts = collections.Counter(right)
    return sum(int(i) * r_counts[i] for i in left)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
