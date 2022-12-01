import numbers


class Elf:
    def __init__(self, calories):
        self.calories = calories

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.calories > other.calories
        elif isinstance(other, numbers.Number):
            return self.calories > other
        else:
            raise NotImplementedError


class Expedition:
    def __init__(self):
        self.elves = []

    def add_elf(self, elf):
        self.elves.append(elf)

    def get_snack_elf(self):
        return max(self.elves)


class CalorieList:
    def __init__(self, input: str):
        self.elf_snack_bags = input.split("\n\n")

    def get_total_calories_in_bag(self, bag):
        calorie_list = [int(item) for item in bag.split("\n")]
        return sum(calorie_list)

    def make_expedition(self):
        self.expedition = Expedition()
        for bag in self.elf_snack_bags:
            calories = self.get_total_calories_in_bag(bag)
            self.expedition.add_elf(Elf(calories))
        return self.expedition


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()
    calorie_list = CalorieList(input_file)
    expedition = calorie_list.make_expedition()
    snack_elf = expedition.get_snack_elf()
    print(snack_elf.calories)
