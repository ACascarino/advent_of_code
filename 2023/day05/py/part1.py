ConstMap = dict[range, int]


class Almanac:
    toc = {
        "seed-to-soil": 0,
        "soil-to-fertiliser": 1,
        "fertiliser-to-water": 2,
        "water-to-light": 3,
        "light-to-temperature": 4,
        "temperature-to-humidity": 5,
        "humidity-to-location": 6,
    }

    def __init__(self, raw_pages: str) -> None:
        pages_txt = raw_pages.split("\n\n")

        self.seeds = self.extract_seeds_from_page_text(pages_txt)
        self.pages = self.read_pages(pages_txt)

    def extract_seeds_from_page_text(self, pages_txt: list[str]) -> list[int]:
        seed_txt = pages_txt[0].split(":")[1].strip()
        return [int(x) for x in seed_txt.split()]

    def read_pages(self, pages_txt: list[str]) -> list[ConstMap]:
        pages = []
        for page_txt in pages_txt[1:]:
            contents = page_txt.splitlines()[1:]
            page = {}
            for line in contents:
                left, right, n = (int(x) for x in line.split())
                domain = range(right, right + n)
                constant = left - right
                page |= {domain: constant}
            pages.append(page)
        return pages

    def lookup(self, value: int, page_no: int) -> int:
        for domain, constant in self.pages[page_no].items():
            if value in domain:
                return value + constant
        return value

    def lookup_through_all_pages(self, value: int) -> int:
        for page_number in range(len(self.toc)):
            value = self.lookup(value, page_number)
        return value


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    almanac = Almanac(puzzle_input)
    print(min(almanac.lookup_through_all_pages(x) for x in almanac.seeds))
