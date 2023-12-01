import part1
from typing import Tuple


def make_collections(iterable, size):
    return zip(*(iter(iterable),) * size)


class TripleRucksack:
    def __init__(self, input: Tuple[str, str, str]) -> None:
        self.rucksacks = map(set, input)

    def get_common_item(self) -> str:
        return set.intersection(*self.rucksacks).pop()


if __name__ == "__main__":
    item_values = part1.generate_item_values()
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    rucksack_contents = puzzle_input.split("\n")
    rucksack_triples = make_collections(rucksack_contents, 3)

    rucksacks = [TripleRucksack(x) for x in rucksack_triples]
    common_item_values = list(
        item_values[rucksack.get_common_item()] for rucksack in rucksacks
    )
    print(sum(common_item_values))
