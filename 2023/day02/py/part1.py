CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}


class GamePart1:
    def __init__(self, game_id: int, rounds: list[str] | tuple[str]) -> None:
        self.game_id = game_id
        self.max_cubes = self.parse_game(rounds)

    def parse_game(self, rounds: list[str] | tuple[str]) -> dict:
        # TODO: There has to be a more elegant solution than this for combining
        cube_usage_per_round = (self.parse_round(round) for round in rounds)
        result = {}
        for round in cube_usage_per_round:
            for colour, number in round.items():
                if number > result.get(colour, 0):
                    result[colour] = number

        return result

    def parse_round(self, round: str) -> dict[str, int]:
        cubes = (self.parse_cube(cube) for cube in round.split(","))
        return {colour: num for cube in cubes for colour, num in cube.items()}

    def parse_cube(self, descriptor: str) -> dict[str, int]:
        number, colour = descriptor.strip().split(" ")
        return {colour: int(number)}

    def possible(self, constraints: dict[str, int]) -> bool:
        # TODO: Again, not in love with this function
        game_is_possible = True
        for constrained_colour, constrained_number in constraints.items():
            if self.max_cubes.get(constrained_colour, 0) > constrained_number:
                game_is_possible = False
        return game_is_possible

    def get_id_if_possible(self, constraints: dict[str, int]) -> bool:
        return self.game_id if self.possible(constraints) else 0


class SessionPart1:
    game_type = GamePart1

    def __init__(self, summary: str) -> None:
        self.games = self.split_session(summary)

    def split_session(self, session: str) -> list[game_type]:
        games = (self.split_game_line(game) for game in session.splitlines())
        return [self.game_type(game_id, rounds) for (game_id, rounds) in games]

    def split_game_line(self, line: str) -> tuple[int, list[str]]:
        (prefix, round_list) = line.split(":")
        game_id = int(prefix.lstrip("Game "))
        rounds = round_list.split(";")
        return (game_id, rounds)

    def sum_possible_games(self, constraints: dict[str, int]) -> int:
        return sum(g.get_id_if_possible(constraints) for g in self.games)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()

    whole_session = SessionPart1(input_file)
    print(whole_session.sum_possible_games(CONSTRAINTS))
