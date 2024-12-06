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

    def fix_if_needs_fixing(self, rules: "Ruleset") -> bool:
        if self.obeys(rules):
            return False
        else:
            self.fix(rules)
            return True

    def fix(self, rules: "Ruleset"):
        rules.rationalise()
        self.pages = sorted(self.pages, key=rules.ranks.get)
        self.middle_page = self.pages[len(self.pages) // 2]


class Ruleset:
    def __init__(self, rules: list[Rule]):
        self.rules = rules
        self.ranks: dict[int, int] = dict()

    def __iter__(self):
        return iter(self.rules)

    def get_rules(self, book: Book) -> "Ruleset":
        return Ruleset([rule for rule in self if all(page in book for page in rule)])

    def rationalise(self) -> None:
        ranks = {
            x: 0
            for x in {
                *(rule.before for rule in self.rules),
                *(rule.after for rule in self.rules),
            }
        }
        changed = True
        while changed == True:
            changed = False
            for rule in self:
                if ranks[rule.before] >= ranks[rule.after]:
                    ranks[rule.before] = ranks[rule.after] - 1
                    changed = True
        self.ranks = ranks


def app(puzzle_input: str) -> int:
    raw_rules, raw_books = [x.splitlines() for x in puzzle_input.split("\n\n")]
    ruleset = Ruleset([Rule(x) for x in raw_rules])
    bookset = [Book(x) for x in raw_books]
    return sum(
        book.middle_page
        for book in bookset
        if book.fix_if_needs_fixing(ruleset.get_rules(book))
    )


if __name__ == "__main__":
    solution = app(aoc_utils.get_input())
    aoc_utils.say(solution)
