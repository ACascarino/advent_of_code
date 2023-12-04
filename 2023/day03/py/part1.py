class SchematicPart1:
    def __init__(self, raw_schematic: str) -> None:
        self.schematic = raw_schematic.splitlines()
        self.n_rows = len(self.schematic) - 1
        self.n_cols = len(self.schematic[0]) - 1  # We assume there is >= 1 row

    def sum_all_part_numbers(self) -> int:
        return sum(self.find_all_part_numbers())

    def find_all_part_numbers(self) -> list[int]:
        return [
            x
            for i, l in enumerate(self.schematic)
            for x in self.find_part_numbers(i, l)
        ]

    def find_part_numbers(self, line_no: int, line: str) -> list[int]:
        part_numbers = []
        numeral_string = ""
        numeral_idxs = []
        in_numeral = False
        for idx, char in enumerate(line):
            if char.isdigit():
                numeral_string += char
                numeral_idxs.append(idx)
                in_numeral = True
            if in_numeral and (not char.isdigit() or idx == self.n_cols):
                in_numeral = False
                if self.is_neighbouring_symbol(line_no, numeral_idxs):
                    part_numbers.append(int(numeral_string))
                numeral_string = ""
                numeral_idxs = []

        return part_numbers

    def is_neighbouring_symbol(self, row: int, cols: list[int]) -> bool:
        l = (min(cols) - 1) if (min(cols) - 1 >= 0) else 0
        r = (max(cols) + 1) if (max(cols) + 1 <= self.n_cols) else self.n_cols
        up = row - 1 if row - 1 >= 0 else None
        down = row + 1 if row + 1 <= self.n_rows else None

        row_up = self.schematic[up][l : r + 1] if up is not None else ""
        row_left = self.schematic[row][l] if l != 0 else ""
        row_right = self.schematic[row][r] if r != self.n_cols else ""
        row_down = self.schematic[down][l : r + 1] if down is not None else ""
        target = row_up + row_left + row_right + row_down

        return self.has_symbol(target)

    def has_symbol(self, chars: str) -> bool:
        # Remove all dots. Does this string have any characters left (truthy)?
        if target := chars.replace(".", ""):
            # If so, anything non-digit is a symbol - find if there are any
            return any((not x.isnumeric() for x in target))
        else:
            # If no characters left, return False
            return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    print(SchematicPart1(puzzle_input).sum_all_part_numbers())
