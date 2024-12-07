import advent_of_code_utils as aoc_utils
from advent_of_code_utils.classes import Point
import typing


class Guard:
    def __init__(self, start_pos: Point):
        self.position = start_pos
        self.direction = Point.Directions.NORTH

    def turn_right(self):
        turn = {
            Point.Directions.NORTH: Point.Directions.EAST,
            Point.Directions.EAST: Point.Directions.SOUTH,
            Point.Directions.SOUTH: Point.Directions.WEST,
            Point.Directions.WEST: Point.Directions.NORTH,
        }
        self.direction = turn[self.direction]

    def advance(self):
        self.position = self.position.travel(self.direction)

    def in_front(self):
        return self.position.travel(self.direction)


class Map:
    def __init__(self, raw_map: list[list[str]]):
        self.field = {
            Point(x, y): Cell(label)
            for y, line in enumerate(raw_map)
            for x, label in enumerate(line)
        }

        self.guard = Guard(next(p for p, c in self.field.items() if c.label == "^"))
        self.visited = {self.guard.position}

    def solve(self):
        while self.guard.in_front() in self.field:
            while self.field[self.guard.in_front()].is_obstruction:
                self.guard.turn_right()
            self.guard.advance()
            self.visited.add(self.guard.position)


class Cell:
    def __init__(self, label: typing.Literal[".", "#", "^"]):
        self.label = label
        self.is_obstruction = label == "#"


def app(puzzle_input: str) -> int:
    raw_map = aoc_utils.input_split_str(puzzle_input)
    map = Map(raw_map)
    map.solve()
    return len(map.visited)


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
