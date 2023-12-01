import part1
from typing import Self


class CorrectRound(part1.Round):
    losing_moves = {"A": "Z", "B": "X", "C": "Y"}
    outcomes = {"X": "loss", "Y": "draw", "Z": "win"}

    def __init__(self: Self, round: str) -> None:
        super().__init__(round)

    def evaluate(self: Self) -> int:
        self.outcome = self.outcomes[self.my_move]
        if self.outcome == "win":
            self.correct_move = self.winning_moves[self.opponent_move]
        elif self.outcome == "draw":
            self.correct_move = self.identical_moves[self.opponent_move]
        else:
            self.correct_move = self.losing_moves[self.opponent_move]

        self.score = (
            self.outcome_score[self.outcome] + self.moves_score[self.correct_move]
        )

        return self.score


class CorrectStrategyGuide(part1.StrategyGuide):
    def __init__(self: Self, guide: str) -> None:
        self.moves = [CorrectRound(x) for x in guide.split("\n")]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()
    guide = CorrectStrategyGuide(puzzle_input)
    print(guide.total())
