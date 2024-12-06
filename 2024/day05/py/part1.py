import advent_of_code_utils as aoc_utils


class Rule:
    def __init__(self, raw_rule: str):
        self.before, self.after = [int(x) for x in raw_rule.split("|")]

    def __contains__(self, item: int) -> bool:
        if isinstance(item, int):
            return item == self.before or item == self.after
        else:
            return NotImplemented

    def __iter__(self):
        return iter((self.before, self.after))

    def __repr__(self) -> str:
        return f"{self.before}|{self.after}"


class Book:
    def __init__(self, raw_book: str):
        self.pages = [int(x) for x in raw_book.split(",")]
        self.middle_page = self.pages[len(self.pages) // 2]

    def __contains__(self, item: int) -> bool:
        if isinstance(item, int):
            return item in self.pages
        else:
            return NotImplemented

    def __iter__(self):
        return iter(self.pages)

    def obeys(self, rules: "Ruleset") -> bool:
        return all(
            self.pages.index(rule.before) < self.pages.index(rule.after)
            for rule in rules
        )


class Ruleset:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def __iter__(self):
        return iter(self.rules)

    def get_rules(self, book: Book) -> "Ruleset":
        return Ruleset([rule for rule in self if all(page in book for page in rule)])


def app(puzzle_input: str) -> int:
    raw_rules, raw_books = [x.splitlines() for x in puzzle_input.split("\n\n")]
    ruleset = Ruleset([Rule(x) for x in raw_rules])
    bookset = [Book(x) for x in raw_books]
    return sum(
        book.middle_page for book in bookset if book.obeys(ruleset.get_rules(book))
    )


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
