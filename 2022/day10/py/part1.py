class Processor:
    def __init__(self) -> None:
        self.pmem = list()
        self.pc = 0
        self.rclk = 0
        self.x = 1
        self.y = 0
        self.instrs = {"addx": self.addx, "noop": self.noop}
        self.rclk_trigger = 0
        self.callback_vector = None
        self.history = {self.rclk: self.x}

    def _add_to_x(self, arg):
        self.x += arg

    def addx(self, args):
        arg = int(args[0])
        self.rclk_trigger = self.rclk + 2
        self.callback_vector = self._add_to_x
        self.y = arg

    def noop(self, args):
        pass

    def set_programme_memory(self, instructions: str):
        for line in instructions.splitlines():
            instr = line.split()
            self.pmem.append((instr[0], instr[1:]))

    def clock(self, cycles):
        for _ in range(cycles):
            self._process()
            self.history |= {self.rclk: self.x}

    def _process(self):
        if self.rclk >= self.rclk_trigger and self.callback_vector is not None:
            self.callback_vector(self.y)
            self.callback_vector = None
        if self.pc is not None and self.callback_vector is None:
            instr, arg = self.pmem[self.pc]
            self.instrs[instr](arg)
            if self.pc < len(self.pmem) - 1:
                self.pc += 1
            else:
                self.pc = None
        self.rclk += 1


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    cpu = Processor()
    cpu.set_programme_memory(puzzle_input)
    cpu.clock(220)

    values_of_interest = (20, 60, 100, 140, 180, 220)
    print(sum(cpu.history[x] * x for x in values_of_interest))
