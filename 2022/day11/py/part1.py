class Item:
    def __init__(self, worry) -> None:
        self.worry = worry


class Monkey:
    def __init__(self, description: str) -> None:
        lines = description.split("\n")
        self.inspect_count = 0

        # Parse the descriptor
        for indx, line in enumerate(lines):
            line = line.strip()
            if line.startswith("Monkey"):
                self.idx = int(line.split()[1].strip(":"))
            elif line.startswith("Starting items"):
                self.items = [Item(int(x)) for x in line.split(": ")[1].split(", ")]
            elif line.startswith("Operation"):
                _, _, _, operation, value = line.split(": ")[1].split()
                # This will be of the form
                #    ["new", "=", "old", "<OPERATION>", "<VALUE>"]
                # Operation can be one of +, -, *, /
                #     Actually, I only see + or * used but there's no stated bounds so...
                # Value can be an int or "old".
                # I miss the operator module.
                self.cb_val = None if value == "old" else int(value)

                if operation == "+":

                    def cb(x: int, y: int) -> int:
                        return x + y

                elif operation == "-":

                    def cb(x: int, y: int) -> int:
                        return x - y

                elif operation == "*":

                    def cb(x: int, y: int) -> int:
                        return x * y

                elif operation == "/":

                    def cb(x: int, y: int) -> int:
                        return x // y

                else:
                    raise NotImplementedError

                self.cb = cb

            elif line.startswith("Test"):
                # This seems to always be "divisible by".
                # I am not going to genericise this.
                self.test_val = int(line.split()[-1])
                # The next two lines will then say which monkey we throw something to.
                self.test_true_monkey = int(lines[indx + 1].split()[-1])
                self.test_false_monkey = int(lines[indx + 2].split()[-1])

    def do_operation(self, item):
        if self.cb_val is None:
            item.worry = self.cb(item.worry, item.worry)
        else:
            item.worry = self.cb(item.worry, self.cb_val)

    def test_item(self, item):
        if not item.worry % self.test_val:
            return self.test_true_monkey
        else:
            return self.test_false_monkey

    def operate_single(self, item):
        self.inspect_count += 1
        self.do_operation(item)
        item.worry //= 3
        return self.test_item(item)

    def operate(self):
        instructions = list()
        while self.items:
            item = self.items.pop(0)
            thrown_to = self.operate_single(item)
            instructions.append((item, thrown_to))
        return instructions


class MonkeyCollection:
    def __init__(self, monkeys) -> None:
        self.monkeys = {monkey.idx: monkey for monkey in monkeys}

    def do_round(self):
        for monkey in self.monkeys.values():
            instructions = monkey.operate()
            while instructions:
                item, thrown_to = instructions.pop(0)
                self.monkeys[thrown_to].items.append(item)

    def total_inspect_counts(self):
        return [monkey.inspect_count for monkey in self.monkeys.values()]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

monkeys = list()

for monkey_desciptor in puzzle_input.split("\n\n"):
    monkeys.append(Monkey(monkey_desciptor))

monkeys = MonkeyCollection(monkeys)

for _ in range(20):
    monkeys.do_round()

inspect_counts = sorted(monkeys.total_inspect_counts(), reverse=True)
print(inspect_counts[0] * inspect_counts[1])
