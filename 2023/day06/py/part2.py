from part1 import Slate


class SlatePart2(Slate):
    def __init__(self, raw_slate: str) -> None:
        times, records = raw_slate.splitlines()
        time = int("".join(times.split()[1:]))
        record = int("".join(records.split()[1:]))

        self.races = [(time, record)]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    slate = SlatePart2(puzzle_input)
    print(slate.multiply_all_good_moves())
