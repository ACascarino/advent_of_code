class Slate:
    def __init__(self, raw_slate: str) -> None:
        times, records = raw_slate.splitlines()
        times = (int(time.strip()) for time in times.split()[1:])
        records = (int(record.strip()) for record in records.split()[1:])
        self.races = zip(times, records)

    def find_number_of_good_moves(self, race: tuple[int, int]) -> int:
        time, record = race
        hold = time // 2
        distance = hold * (time - hold)
        number = 0  # We assume that there is a good move...
        while distance > record:
            number += 1
            hold -= 1
            distance = hold * (time - hold)
        return number * 2 - (0 if time % 2 else 1)

    def multiply_all_good_moves(self) -> int:
        result = 1
        for race in self.races:
            result *= self.find_number_of_good_moves(race)
        return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    slate = Slate(puzzle_input)
    print(slate.multiply_all_good_moves())
