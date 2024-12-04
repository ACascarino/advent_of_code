import advent_of_code_utils as aoc_utils
import re


def app(puzzle_input: str) -> int:
    search_string = r"mul\((\d*?),(\d*?)\)"
    found = re.findall(search_string, puzzle_input)
    accs = (int(a) * int(b) for a, b in found)
    return sum(accs)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
