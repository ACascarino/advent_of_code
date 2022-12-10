def ceil_int_div(a, b):
    # If a is divisible by b, then return the dividend
    # Else, if the dividend is positive, add one then return.
    if not a % b:
        return a // b
    else:
        dividend = a // b
        return dividend if dividend < 0 else dividend + 1


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Vector2):
            if self.x == __o.x and self.y == __o.y:
                return True
            else:
                return False
        else:
            raise NotImplementedError

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def copy(self):
        return type(self)(self.x, self.y)


class Direction(Vector2):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


class Coordinate(Vector2):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def __add__(self, a):
        if isinstance(a, Direction):
            return Coordinate(self.x + a.x, self.y + a.y)
        else:
            raise NotImplementedError

    def __iadd__(self, a):
        if isinstance(a, Direction):
            self.x += a.x
            self.y += a.y
            return self
        else:
            raise NotImplementedError

    def __sub__(self, a):
        if isinstance(a, Direction):
            return Coordinate(self.x - a.x, self.y - a.y)
        elif isinstance(a, Coordinate):
            return Direction(self.x - a.x, self.y - a.y)
        else:
            raise NotImplementedError

    def distance(self, a):
        if isinstance(a, Coordinate):
            x_distance, y_distance = map(abs, self - a)
            return max(x_distance, y_distance)


class Rope:
    def __init__(self, length) -> None:
        self.knots = [Knot(self, 0, 0) for _ in range(length)]
        self.head = self.knots[0]
        self.tail = self.knots[-1]
        self.visited = {Coordinate(0, 0)}

        for idx, knot in enumerate(self.knots):
            if knot is self.head:
                knot.parent = None
                knot.child = self.knots[idx + 1]
            elif knot is self.tail:
                knot.parent = self.knots[idx - 1]
                knot.child = None
            else:
                knot.parent = self.knots[idx - 1]
                knot.child = self.knots[idx + 1]

    def move_head(self, direction: str):
        self.head.move(directions[direction])

    def move_head_x(self, direction: str, number):
        for _ in range(number):
            self.move_head(direction)


class Knot(Coordinate):
    def __init__(self, rope, x, y) -> None:
        super().__init__(x, y)
        self.rope = rope
        self.parent = None
        self.child = None

    def move(self, direction: Direction):
        self += direction
        if self.child is not None:
            self.move_child()
        else:
            self.rope.visited.add(Coordinate(self.x, self.y))

    def move_child(self):
        distance = self.child.distance(self)
        if distance > 1:
            # If done correctly, distance should always be in the set {0, 1, 2}
            # Therefore, this branch can make the assumption that distance == 2.
            # There are 3 possible families of x, y distances in this case - both 2, one 0 and one 2, or one 1 and one 2 (or negative versions thereof)
            # In all cases, if we divide both by 2 and take the ceiling of the outcome, we get the desired movement vector.
            # Finally, update the set of inhabited coordinates.
            x_distance, y_distance = self - self.child
            vector = Direction(ceil_int_div(x_distance, 2), ceil_int_div(y_distance, 2))
            self.child.move(vector)
        else:
            return


class MovementInstructions:
    def __init__(self, instructions: str) -> None:
        instruction_lines = instructions.splitlines()
        self.instructions = (
            (direction, int(number))
            for direction, number in (line.split() for line in instruction_lines)
        )

    def __iter__(self):
        for instruction in self.instructions:
            yield instruction


directions: dict[str:Direction] = {
    "L": Direction(-1, 0),
    "U": Direction(0, 1),
    "R": Direction(1, 0),
    "D": Direction(0, -1),
}

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    instructions = MovementInstructions(puzzle_input)
    rope = Rope(10)
    for dir, number in instructions:
        rope.move_head_x(dir, number)
    print(len(rope.visited))
