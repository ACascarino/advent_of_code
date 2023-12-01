from typing import Self


class Round:
    identical_moves = {"A": "X", "B": "Y", "C": "Z"}
    winning_moves = {"A": "Y", "B": "Z", "C": "X"}
    outcome_score = {"win": 6, "draw": 3, "loss": 0}
    moves_score = {"X": 1, "Y": 2, "Z": 3}

    def __init__(self: Self, round: str) -> None:
        self.opponent_move, self.my_move = round.split(" ")

    def evaluate(self: Self) -> int:
        if self.identical_moves[self.opponent_move] == self.my_move:
            self.outcome = "draw"
        elif self.winning_moves[self.opponent_move] == self.my_move:
            self.outcome = "win"
        else:
            self.outcome = "loss"

        self.score = self.outcome_score[self.outcome] + self.moves_score[self.my_move]

        return self.score


class StrategyGuide:
    def __init__(self: Self, guide: str) -> None:
        self.moves = [Round(x) for x in guide.split("\n")]

    def total(self) -> int:
        round_totals = list(round.evaluate() for round in self.moves)
        return sum(round_totals)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    guide = StrategyGuide(puzzle_input)
    print(guide.total())
