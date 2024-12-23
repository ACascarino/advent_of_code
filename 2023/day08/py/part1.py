import advent_of_code_utils as aoc_utils
import ast

DIRECTIONS = {"L": 0, "R": 1}


def build_network(nodes: list[str]) -> dict[str, tuple[str, str]]:
    network = {}
    for route in nodes:
        node, directions = [part.strip() for part in route.split("=")]
        left, right = ast.literal_eval(
            directions.replace("(", "('").replace(", ", "','").replace(")", "')")
        )
        network |= {node: (left, right)}
    return network


def app(puzzle_input: str) -> int:
    lines = [line.strip() for line in puzzle_input.splitlines() if line]
    instructions, *nodes = lines
    network = build_network(nodes)

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        direction = DIRECTIONS[instructions[steps % len(instructions)]]
        current_node = network[current_node][direction]
        steps += 1

    return steps


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
