from part1 import SchematicPart1


class SchematicPart2(SchematicPart1):
    def __init__(self, raw_schematic: str) -> None:
        super().__init__(raw_schematic)
        self.star_chart: dict[tuple[int, int], list[int]] = {}

    def get_part_num_from_idxs(self, row: int, cols: list[int]) -> int:
        return int(self.schematic[row][min(cols) : max(cols) + 1])

    def is_neighbouring_symbol(self, row: int, cols: list[int]) -> bool:
        result, star = super().is_neighbouring_symbol(row, cols)
        if star:
            self.update_star_chart(row, cols)
        return result

    def update_star_chart(self, row: int, cols: list[int]):
        # Horrible hacky search but I'm bored of this puzzle now (10th Dec)
        l, r, u, d = self.get_neighbour_idxs(row, cols)
        up, left, right, down = self.get_adjacent(l, r, u, row, d)
        part_num = self.get_part_num_from_idxs(row, cols)
        if "*" in left:
            target = (row, l)
        elif "*" in right:
            target = (row, r)
        elif "*" in up:
            target = (u, self.schematic[u].find("*", l, r + 1))
        elif "*" in down:
            target = (d, self.schematic[d].find("*", l, r + 1))
        existing = self.star_chart.get(target, [])
        self.star_chart |= {target: existing + [part_num]}

    def get_gear_ratio(self, *args: int) -> int:
        if len(args) != 2:
            return 0
        else:
            return args[0] * args[1]

    def sum_all_gear_ratios(self) -> int:
        self.find_all_part_numbers()
        return sum(self.get_gear_ratio(*p) for p in self.star_chart.values())

    def has_symbol(self, chars: str) -> tuple[bool, bool]:
        result = super().has_symbol(chars)
        return (result, "*" in chars)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    schem = SchematicPart2(puzzle_input)
    print(schem.sum_all_gear_ratios())
