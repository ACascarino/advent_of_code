import part1
from typing import Tuple


class TripleRucksack(part1.Rucksack):
    def __init__(self, input: Tuple[str, str, str]) -> None:
        self.rucksacks = map(set, input)

    def get_common_items(self):
        return set.intersection(*self.rucksacks)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    rucksack_contents = puzzle_input.split("\n")
    rucksack_triples = []
    for idx in range(len(rucksack_contents) // 3):
        triple = []
        for rucksack in range(3):
            triple.append(rucksack_contents.pop(0))
        rucksack_triples.append(tuple(triple))

    rucksacks = [TripleRucksack(x) for x in rucksack_triples]
    common_item_values = list(
        rucksack.get_item_value(rucksack.get_common_items().pop())
        for rucksack in rucksacks
    )
    print(sum(common_item_values))
