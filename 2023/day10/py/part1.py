import advent_of_code_utils as aoc_utils
from advent_of_code_utils.classes import Point
import math
import typing


class Pipe:

    _connects = {
        "|": ((0, -1), (0, 1)),
        "-": ((-1, 0), (1, 0)),
        "L": ((0, -1), (1, 0)),
        "J": ((0, -1), (-1, 0)),
        "7": ((-1, 0), (0, 1)),
        "F": ((1, 0), (0, 1)),
    }

    def __init__(
        self,
        location: Point,
        label: typing.Literal["|", "-", "L", "J", "7", "F", ".", "S"],
    ):
        self.location = location
        self.label = label
        self.connecting_points = self.connections(label)
        self.is_starting_node = label == "S"

    def __repr__(self) -> str:
        return self.label

    def connects_with(self, other_pipe: "Pipe") -> bool:
        return (
            other_pipe.location in self.connecting_points
            if self.connecting_points is not None
            else None
        )

    def connections(
        self, label: typing.Literal["|", "-", "L", "J", "7", "F", ".", "S"]
    ) -> tuple[Point, Point] | None:
        if (connections := self._connects.get(label, None)) is None:
            return None
        else:
            return tuple(self.location + connection for connection in connections)


class Grid:
    def __init__(self, raw_field: list[list[str]]) -> None:
        self.field = {
            Point(x, y): Pipe(Point(x, y), label)
            for y, line in enumerate(raw_field)
            for x, label in enumerate(line)
        }

        starting_point, starting_pipe = next(
            (point, pipe) for point, pipe in self.field.items() if pipe.is_starting_node
        )
        previous_point = next_point = starting_point

        # Work out in which direction to start moving
        if (
            north_pipe := self.field.get(starting_point.north(), None)
        ) is not None and north_pipe.connects_with(starting_pipe):
            next_point = starting_point.north()
        elif (
            east_pipe := self.field.get(starting_point.east(), None)
        ) is not None and east_pipe.connects_with(starting_pipe):
            next_point = starting_point.east()
        else:
            # If north and east do not connect, south and west must.
            next_point = starting_point.south()

        loop_points: list[Point] = []

        while next_point != starting_point:
            loop_points.append(next_point)
            current_point = next_point

            next_pipe = self.field[next_point]
            next_point = next(
                c for c in next_pipe.connecting_points if c != previous_point
            )
            previous_point = current_point

        self.loop_length = len(loop_points)


def app(puzzle_input: str) -> int:
    raw_field = aoc_utils.input_split_str(puzzle_input)
    field = Grid(raw_field)
    return math.ceil(field.loop_length / 2)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
