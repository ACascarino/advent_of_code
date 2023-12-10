class Card:
    def __init__(self, line: str) -> None:
        self.card_id, self.winning, self.has = self.parse_line(line)
        self.winning_values = set(self.winning) & set(self.has)
        self.points = self.calculate_points(self.winning_values)

    def parse_line(self, line: str) -> tuple[int, list[int], list[int]]:
        id_segment, num_segment = (x.strip() for x in line.split(":"))
        card_id = int(id_segment.strip("Card "))
        win_segment, has_segment = (x.strip() for x in num_segment.split("|"))
        card_win = [int(x) for x in win_segment.split()]
        card_has = [int(x) for x in has_segment.split()]
        return card_id, card_win, card_has

    def calculate_points(self, winning_values) -> int:
        if (overlap := len(winning_values)) != 0:
            return 2 ** (overlap - 1)
        else:
            return 0


class CardPile:
    def __init__(self, list_of_cards: str) -> None:
        self.cards = [Card(l) for l in list_of_cards.splitlines()]

    def sum_points(self) -> int:
        return sum(c.points for c in self.cards)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    pile = CardPile(puzzle_input)
    print(pile.sum_points())
