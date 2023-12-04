from part1 import SchematicPart1


class SchematicPart2(SchematicPart1):
    def has_symbol(self, chars: str) -> bool:
        # Remove all dots. Does this string have any characters left (truthy)?
        if target := chars.replace(".", ""):
            # If so, anything non-digit is a symbol - find if there are any.
            return any((not x.isnumeric() for x in target))
        else:
            # If no characters left, return False
            return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    print(SchematicPart2(puzzle_input).sum_all_part_numbers())
