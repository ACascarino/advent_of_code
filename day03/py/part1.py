from typing import Tuple


def split_string_in_half(input: str) -> Tuple[str, str]:
    string_length = len(input)
    if string_length % 2:
        raise NotImplementedError
    return (input[: string_length // 2], input[string_length // 2 :])


def generate_item_values() -> dict:
    item_values = {}
    for x in range(65, 91):
        item_values |= {chr(x): x - (64 - 26)}
    for x in range(97, 123):
        item_values |= {chr(x): x - 96}
    return item_values


class Rucksack:
    def __init__(self, input: str) -> None:
        self.comp_one, self.comp_two = map(set, split_string_in_half(input))

    def get_common_item(self) -> str:
        return set.intersection(self.comp_one, self.comp_two).pop()


if __name__ == "__main__":
    item_values = generate_item_values()

    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    rucksacks = [Rucksack(x) for x in puzzle_input.split("\n")]
    common_item_values = list(
        item_values[rucksack.get_common_item()] for rucksack in rucksacks
    )
    print(sum(common_item_values))
