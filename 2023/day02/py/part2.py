from part1 import GamePart1, SessionPart1

POWERFUL_COLOURS = ("red", "green", "blue")


class GamePart2(GamePart1):
    def get_power(self, powerful_colours: tuple[str]):
        # TODO: SURELY there's a better way than this
        power = 1
        for colour in powerful_colours:
            power *= self.max_cubes.get(colour, 0)
        return power


class SessionPart2(SessionPart1):
    game_type = GamePart2

    def get_power_sum(self, powerful_colours: tuple[str]):
        return sum(game.get_power(powerful_colours) for game in self.games)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()

    whole_session = SessionPart2(input_file)
    print(whole_session.get_power_sum(POWERFUL_COLOURS))
