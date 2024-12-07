import advent_of_code_utils as aoc_utils
from advent_of_code_utils.classes import Point
import typing


class Guard:
    def __init__(self, start_pos: Point):
        self.starting_position = start_pos
        self.reset()

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

    def reset(self):
        self.position = self.starting_position
        self.direction = Point.Directions.NORTH


class Map:
    def __init__(self, raw_map: list[list[str]]):
        self.field = {
            Point(x, y): Cell(label)
            for y, line in enumerate(raw_map)
            for x, label in enumerate(line)
        }

        self.guard = Guard(next(p for p, c in self.field.items() if c.label == "^"))
        self.visited_first_time = set()

    def solve(self) -> set[Point]:
        visited = {self.guard.position}
        while self.guard.in_front() in self.field:
            while self.field[self.guard.in_front()].is_obstruction:
                self.guard.turn_right()
            self.guard.advance()
            visited.add(self.guard.position)
        return visited

    def calculate_loops(self) -> int:
        # Starting position can't be an obstruction
        self.visited_first_time.remove(self.guard.starting_position)
        n_obstructions = 0
        for i, p in enumerate(self.visited_first_time):
            print(f"Run {i}/{len(self.visited_first_time)}")
            self.guard.reset()
            # All places passed through are only candidates for obstructions
            in_loop = False
            self.field[p].is_obstruction = True
            visited = {(self.guard.position, self.guard.direction)}
            while (self.guard.in_front() in self.field) and (in_loop == False):
                while self.field[self.guard.in_front()].is_obstruction:
                    self.guard.turn_right()
                self.guard.advance()
                if (self.guard.position, self.guard.direction) in visited:
                    n_obstructions += 1
                    in_loop = True
                else:
                    visited.add((self.guard.position, self.guard.direction))
            self.field[p].is_obstruction = False
        return n_obstructions


class Cell:
    def __init__(self, label: typing.Literal[".", "#", "^"]):
        self.label = label
        self.is_obstruction = label == "#"


def app(puzzle_input: str) -> int:
    raw_map = aoc_utils.input_split_str(puzzle_input)
    map = Map(raw_map)
    map.visited_first_time = map.solve()
    return map.calculate_loops()


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
