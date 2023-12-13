class Hand:
    hand_types = {
        "five_of_a_kind": 7,
        "four_of_a_kind": 6,
        "full_house": 5,
        "three_of_a_kind": 4,
        "two_pair": 3,
        "one_pair": 2,
        "high_card": 1,
    }

    card_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = bid
        self.hand_type = self.determine_hand_type()

    def __repr__(self) -> str:
        return self.cards

    def determine_hand_type(self) -> int:
        num_distinct_cards = len(set(self.cards))
        if num_distinct_cards == 5:
            return self.hand_types["high_card"]
        elif num_distinct_cards == 4:
            return self.hand_types["one_pair"]
        elif num_distinct_cards == 1:
            return self.hand_types["five_of_a_kind"]
        elif num_distinct_cards == 2:
            # Either 4oaK or FH.
            # For 4oaK, either 4 or 1 of first card. For FH, either 2 or 3.
            num_first_card = self.cards.count(self.cards[0])
            if num_first_card == 4 or num_first_card == 1:
                return self.hand_types["four_of_a_kind"]
            else:
                return self.hand_types["full_house"]
        else:
            # Either 3oaK or 2P
            num_first_card = self.cards.count(self.cards[0])
            if num_first_card == 3:
                # If there's 3 of the first character, must be 3oaK.
                return self.hand_types["three_of_a_kind"]
            elif num_first_card == 2:
                # If there's 2 of the first character, must be 2P.
                return self.hand_types["two_pair"]
            else:
                # If there's 1 of the first character, check second.
                num_second_card = self.cards.count(self.cards[1])
                if num_second_card == 3:
                    # If 3 of second character, must be 3oaK.
                    return self.hand_types["three_of_a_kind"]
                elif num_second_card == 2:
                    # If 2 of second character, must be 2P.
                    return self.hand_types["two_pair"]
                else:
                    # If 1 of second character, check third.
                    num_third_card = self.cards.count(self.cards[2])
                    if num_third_card == 3:
                        # If 3 of third character, must be 3oaK.
                        return self.hand_types["three_of_a_kind"]
                    else:
                        # If 2 of third character, must be 2P.
                        return self.hand_types["two_pair"]

    def evaluate_hand(self) -> int:
        """
        Gives a unique value per hand, where A2222 > KAAAA etc.
        """
        values = [self.card_values[x] for x in self.cards]
        idxs = len(self.cards) - 1
        log2_card_v = 4  # 14 total card values, so takes 4 bits to store them
        return sum(v << log2_card_v * (idxs - i) for i, v in enumerate(values))


class Tableau:
    hand_class = Hand

    def __init__(self, raw_tableau: str) -> None:
        raw_hands = raw_tableau.splitlines()
        self.hands = [self.hand_class(*self.parse_hand(l)) for l in raw_hands]

    def parse_hand(self, raw_hand: str) -> tuple[str, int]:
        raw_cards, raw_bid = (x.strip() for x in raw_hand.split())
        return (raw_cards, int(raw_bid))

    def sort_hands(self) -> None:
        self.hands.sort(key=lambda h: h.evaluate_hand())
        self.hands.sort(key=lambda h: h.hand_type)

    def get_total_winnings(self) -> int:
        return sum(hand.bid * (idx + 1) for idx, hand in enumerate(self.hands))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    tableau = Tableau(puzzle_input)
    tableau.sort_hands()
    print(tableau.get_total_winnings())
