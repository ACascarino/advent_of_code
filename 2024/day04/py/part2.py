import advent_of_code_utils as aoc_utils
import re
import typing


SS = 0
SM = 1
MS = 2
MM = 3


MAS_COUNTERPARTS = {
    SS: MM,
    SM: SM,
    MS: MS,
    MM: SS,
}


def non_none(check: tuple[typing.Any | None, ...]) -> int:
    return [i for i, x in enumerate(check) if x is not None][0]


def app(puzzle_input: str) -> int:
    lines = puzzle_input.splitlines()
    all_matches: list[
        dict[int, tuple[str | None, str | None, str | None, str | None]]
    ] = []
    solution = 0

    for line in lines:
        matches = re.finditer(r"(?=(S.S)|(S.M)|(M.S)|(M.M))", line)
        all_matches.append({match.start(): match.groups() for match in matches})

    for line_no, match_set in enumerate(all_matches[:-2]):
        for char_no, ends in match_set.items():
            matched = non_none(ends)
            # is there a match at the same position 2 lines down?
            if char_no in all_matches[line_no + 2]:
                # is it complementary?
                other_end = all_matches[line_no + 2][char_no]
                other_matched = non_none(other_end)
                if MAS_COUNTERPARTS[matched] == other_matched:
                    # is there an A in the middle?
                    if lines[line_no + 1][char_no + 1] == "A":
                        solution += 1

    return solution


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
