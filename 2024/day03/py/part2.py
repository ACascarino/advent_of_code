import advent_of_code_utils as aoc_utils
import re


def app(puzzle_input: str) -> int:
    search_string = r"(?:mul\((\d*?),(\d*?)\))|(do\(\))|(don't\(\))"
    solution = 0
    mul = True
    for found in re.findall(search_string, puzzle_input):
        match found:
            case ("", "", "", "don't()"):
                mul = False
            case ("", "", "do()", ""):
                mul = True
            case (a, b, "", ""):
                if mul:
                    solution += int(a) * int(b)
    return solution


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
