import advent_of_code_utils as aoc_utils
import itertools


def predict_future(chronicle: list[list[int]]) -> int:
    layer = -1
    final_layer = -len(chronicle)
    while layer != final_layer:
        layer -= 1
        chronicle[layer].append(chronicle[layer][-1] + chronicle[layer + 1][-1])
    return chronicle[0][-1]


def app(puzzle_input: str) -> int:
    solution = 0
    histories = aoc_utils.input_split_int(puzzle_input)
    for history in histories:
        chronicle = [history]
        while not all(value == 0 for value in chronicle[-1]):
            diffs = [b - a for a, b in itertools.pairwise(chronicle[-1])]
            chronicle.append(diffs)

        solution += predict_future(chronicle)
    return solution


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
