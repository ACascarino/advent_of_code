from part1 import Card, CardPile


class CardPilePart2(CardPile):
    def win_scratchcards(self) -> None:
        for card in self.cards:
            new_cards = self.determine_winnings(card)
            self.cards.extend(new_cards)

    def determine_winnings(self, card: Card) -> list[int]:
        """
        This very much relies on the input string being ordered and 1-indexed.
        """
        winnings = len(card.winning_values)
        return [self.cards[card.card_id + x] for x in range(winnings)]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    pile = CardPilePart2(puzzle_input)
    pile.win_scratchcards()
    print(len(pile.cards))
