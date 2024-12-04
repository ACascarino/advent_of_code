import advent_of_code_utils as aoc_utils
import re


def app(puzzle_input: str) -> int:
    search_string = r"(mul\((%d*?),(%d*?)\))|(do\(\))|(don't\(\))"
    found = re.findall(search_string, puzzle_input)
    aoc_utils.say([found])


if __name__ == "__main__":
    solution = app(aoc_utils.get_test())
    aoc_utils.say(solution)
