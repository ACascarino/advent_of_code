def range1(start, end):
    return range(start, end + 1)


class Pair:
    def __init__(self, line) -> None:
        left, right = line.split(",")
        self.left_range = set(range1(*map(int, left.split("-"))))
        self.right_range = set(range1(*map(int, right.split("-"))))

    def is_there_full_overlap(self):
        if self.left_range >= self.right_range or self.right_range >= self.left_range:
            return True
        else:
            return False


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    pairs = [Pair(x) for x in puzzle_input.split("\n")]
    print(sum(x.is_there_full_overlap() for x in pairs))
