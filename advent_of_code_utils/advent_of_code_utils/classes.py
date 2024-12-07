import enum
import typing


class Point:
    class Directions(enum.Enum):
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: tuple[int, int]) -> "Point":
        if isinstance(other, tuple) and len(other) == 2:
            return Point(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented

    def __eq__(self, value: typing.Union["Point", tuple[int, int]]) -> bool:
        if isinstance(value, Point):
            return self.x == value.x and self.y == value.y
        elif isinstance(value, tuple) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def up(self) -> "Point":
        return Point(self.x, self.y - 1)

    def down(self) -> "Point":
        return Point(self.x, self.y + 1)

    def left(self) -> "Point":
        return Point(self.x - 1, self.y)

    def right(self) -> "Point":
        return Point(self.x + 1, self.y)

    def north(self) -> "Point":
        return self.up()

    def south(self) -> "Point":
        return self.down()

    def east(self) -> "Point":
        return self.right()

    def west(self) -> "Point":
        return self.left()

    def travel(
        self,
        direction: typing.Literal[
            Directions.NORTH, Directions.EAST, Directions.SOUTH, Directions.WEST
        ],
    ):
        return (self.north, self.east, self.south, self.west)[direction.value]()
