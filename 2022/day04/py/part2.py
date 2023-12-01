import part1


class OverlappingPair(part1.Pair):
    def __init__(self, line: str) -> None:
        super().__init__(line)

    def is_there_any_overlap(self) -> bool:
        if set.intersection(self.left_range, self.right_range):
            return True
        else:
            return False


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    pairs = [OverlappingPair(x) for x in puzzle_input.split("\n")]
    print(sum(x.is_there_any_overlap() for x in pairs))
