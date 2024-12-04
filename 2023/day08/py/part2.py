import advent_of_code_utils as aoc_utils
import ast
import math

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

    current_nodes = [node for node in network.keys() if node.endswith("A")]
    loop_counts = [None] * len(current_nodes)
    steps = 0

    while not all(count is not None for count in loop_counts):
        direction = DIRECTIONS[instructions[steps % len(instructions)]]
        steps += 1
        for i, node in enumerate(current_nodes):
            new_node = current_nodes[i] = network[node][direction]
            if new_node.endswith("Z"):
                loop_counts[i] = steps

    return math.lcm(*loop_counts)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
