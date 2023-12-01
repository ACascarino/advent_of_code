import part1


class Crt:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.display = [[0 for _ in range(width)] for _ in range(height)]

    def set_graphical_memory(self, info):
        self.gmem = info

    def clock(self, cycles):
        for cycle in range(cycles):
            self._process(cycle + 1)

    def _process(self, cycle):
        horz = (cycle - 1) % 40
        vert = (cycle - 1) // 40
        x = self.gmem[cycle]

        current_sprite_pos = (x - 1, x, x + 1)

        self.display[vert][horz] = 1 if horz in current_sprite_pos else 0

    def render(self):
        for line in self.display:
            print("".join("#" if pixel else "." for pixel in line))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    cpu = part1.Processor()
    cpu.set_programme_memory(puzzle_input)
    cpu.clock(240)

    crt = Crt(width=40, height=6)
    crt.set_graphical_memory(cpu.history)
    crt.clock(240)
    crt.render()
