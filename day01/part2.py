import part1
import numbers


class SortableElf(part1.Elf):
    def __init__(self, calories):
        super().__init__(calories)

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.calories > other.calories
        elif isinstance(other, numbers.Number):
            return self.calories > other
        else:
            raise NotImplementedError


class SensibleExpedition(part1.Expedition):
    def __init__(self):
        super().__init__()

    def get_top_elves(self, x):
        sorted_elves = sorted(self.elves)
        return (sorted_elves[idx] for idx in range(x))


class FuckItImTired(part1.CalorieList):
    def __init__(self, input: str):
        super().__init__(input)

    def make_sensible_expedition(self):
        self.expedition = SensibleExpedition()
        for bag in self.elf_snack_bags:
            calories = self.get_total_calories_in_bag(bag)
            self.expedition.add_elf(SortableElf(calories))
        return self.expedition


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()
    calorie_list = FuckItImTired(input_file)
    expedition = calorie_list.make_sensible_expedition()
    snack_elves = expedition.get_top_elves(3)
    print(sum(elf.calories for elf in snack_elves))
