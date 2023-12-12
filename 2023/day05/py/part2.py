from part1 import Almanac
from time import perf_counter_ns

p = (0, 1, 2, 3, 4, 5, 6)


class AlmanacPart2(Almanac):
    def read_pages(self, pages_txt: list[str]):
        pages = []
        for page_txt in pages_txt[1:]:
            contents = page_txt.splitlines()[1:]
            page = {}
            for line in contents:
                left, right, n = (int(x) for x in line.split())
                domain = range(left, left + n)
                constant = right - left
                page |= {domain: constant}
            pages.append(page)
        return list(reversed(pages))

    def reverse_pages(self, target: int) -> int:
        for idx in p:
            target = self.reverse_lookup(idx, target)
        return target

    def reverse_lookup(self, page_no: int, value: int) -> int:
        for domain, constant in self.pages[page_no].items():
            if (value - constant) in domain:
                return value - constant
        return value

    def convert_seed_list(self) -> list[range]:
        seeds_paired = zip(self.seeds[::2], self.seeds[1::2])
        return [range(start, start + length) for start, length in seeds_paired]

    def lookup_through_all_pages(self, value: int) -> int:
        for page_number in p:
            value = self.lookup(value, page_number)
        return value

    def find_lowest_valid_output(self, targets: list[range]) -> int:
        location = 0
        while True:
            # tic = perf_counter_ns()
            result = self.lookup_through_all_pages(location)
            for target in targets:
                if result in target:
                    return location
            location += 1
            # toc = perf_counter_ns()
            # print(toc - tic)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    almanac = AlmanacPart2(puzzle_input)
    new_seeds = almanac.convert_seed_list()
    toc = perf_counter_ns()
    print(almanac.find_lowest_valid_output(new_seeds))
    tic = perf_counter_ns()
    print(tic - toc)
