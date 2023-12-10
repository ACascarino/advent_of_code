from part1 import Almanac


class AlmanacPart2(Almanac):
    def convert_seed_list(self) -> list[range]:
        seeds_paired = zip(self.seeds[::2], self.seeds[1::2])
        return [range(start, start + length) for start, length in seeds_paired]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    almanac = AlmanacPart2(puzzle_input)
    i = almanac.convert_seed_list()
    print(i)
    print(min(almanac.lookup_through_all_pages(c) for run in i for c in run))
