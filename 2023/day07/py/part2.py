from part1 import Hand, Tableau


class HandPart2(Hand):
    def __init__(self, cards: str, bid: int) -> None:
        super().__init__(cards, bid)
        self.card_values["J"] = 1

    def determine_hand_type(self) -> int:
        old = super().determine_hand_type()
        if "J" not in self.cards:
            return old
        else:
            num_j = self.cards.count("J")
            if old == self.hand_types["high_card"]:
                # If it was "high card", J makes 1P
                return self.hand_types["one_pair"]
            elif old == self.hand_types["one_pair"]:
                # If it was "one pair", J makes a 3oaK
                return self.hand_types["three_of_a_kind"]
            elif old == self.hand_types["two_pair"]:
                # If it was "two pair", count Js.
                if num_j == 1:
                    # If J wasn't in the pairs, makes FH
                    return self.hand_types["full_house"]
                else:
                    # Only other option is J was one of the pairs - makes 4oaK
                    return self.hand_types["four_of_a_kind"]
            elif old == self.hand_types["three_of_a_kind"]:
                # If it was "three of a kind", J makes a 4oaK
                return self.hand_types["four_of_a_kind"]
            else:
                # If it was "full house", "four of a kind", or "five of a kind"
                # J makes 5oaK
                return self.hand_types["five_of_a_kind"]


class TableauPart2(Tableau):
    hand_class = HandPart2


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    tableau = TableauPart2(puzzle_input)
    tableau.sort_hands()
    print(tableau.get_total_winnings())
