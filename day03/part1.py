from typing import Tuple


def split_string_in_half(input: str) -> Tuple[str, str]:
    string_length = len(input)
    if string_length % 2:
        raise NotImplementedError
    return (input[: string_length // 2], input[string_length // 2 :])


class Rucksack:
    def __init__(self, input: str) -> None:
        self.comp_one, self.comp_two = map(set, split_string_in_half(input))

    def get_common_items(self):
        return self.comp_one.intersection(self.comp_two)

    def get_item_value(self, item: str):
        if item.islower():
            return ord(item) - 96
        else:
            return ord(item) - (64 - 26)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    rucksacks = [Rucksack(x) for x in puzzle_input.split("\n")]
    common_item_values = list(
        rucksack.get_item_value(rucksack.get_common_items().pop())
        for rucksack in rucksacks
    )
    print(sum(common_item_values))
