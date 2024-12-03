from __future__ import annotations

DIRS = {
    "up_left": (-1, -1),
    "up": (0, -1),
    "up_right": (1, -1),
    "right": (1, 0),
    "down_right": (1, 1),
    "down": (0, 1),
    "down_left": (-1, 1),
    "left": (-1, 0),
}


def tuple_add(tup1: tuple[int, ...], tup2: tuple[int, ...]) -> tuple[int, ...]:
    if len(tup1) != len(tup2):
        raise ValueError
    result = []
    for a, b in zip(tup1, tup2):
        result.append(a + b)
    return tuple(result)


class Octopus:
    def __init__(self, parent: OctopusCollection, energy: int, x: int, y: int) -> None:
        self.parent = parent
        self.energy = energy
        self.x = x
        self.y = y
        self.flashed = False

    def check_flash(self) -> bool:
        if self.energy > 9 and not self.flashed:
            self.flash()
            return True
        return False

    def flash(self) -> None:
        self.flashed = True

    def get_neighbours(self) -> list[Octopus]:
        return self.parent.get_neighbours(self.x, self.y)

    def energise(self) -> None:
        self.energy += 1

    def reset(self) -> int:
        if self.flashed:
            self.energy = 0
            self.flashed = False
            return 1
        return 0

    def __repr__(self) -> str:
        return f"{self.energy}"


class OctopusCollection:
    def __init__(self) -> None:
        self.data: list[list[Octopus]] = []
        self.flashes = 0

    def parse(self, in_text: str) -> None:
        data = []
        for y, line in enumerate(in_text.split("\n")):
            contents = [int(x) for x in line]
            if contents:
                row = []
                for x, energy in enumerate(contents):
                    row.append(Octopus(self, energy, x, y))
                data.append(row)
        self.x_max = x
        self.y_max = y - 1
        self.data = data

    def report(self) -> None:
        for line in self.data:
            print(line)
        print(self.flashes)

    def increase(self) -> None:
        for line in self.data:
            for octopus in line:
                octopus.energise()

    def do_flash(self) -> None:
        tracked: list[Octopus] = []
        for line in self.data:
            for octopus in line:
                tracked.append(octopus)
        while tracked:
            octopus = tracked.pop()
            flashed = octopus.check_flash()
            if flashed:
                neighbours = octopus.get_neighbours()
                for neighbour in neighbours:
                    neighbour.energise()
                tracked += neighbours

    def end_step(self) -> None:
        for line in self.data:
            for octopus in line:
                self.flashes += octopus.reset()

    def get_neighbours(self, x: int, y: int) -> list[Octopus]:
        result = []
        for dir in DIRS.values():
            x_t, y_t = tuple_add(dir, (x, y))
            if x_t > self.x_max or x_t < 0 or y_t > self.y_max or y_t < 0:
                continue
            result.append(self.data[y_t][x_t])
        return result

    def advance(self, steps) -> None:
        for i in range(steps):
            self.increase()
            self.do_flash()
            self.end_step()


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    cave = OctopusCollection()
    cave.parse(input)
    cave.advance(100)
    cave.report()
