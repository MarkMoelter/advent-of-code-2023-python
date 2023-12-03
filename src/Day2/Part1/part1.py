from Day2.Part1.game import Game


class Part1:
    def __init__(self, num_rgb: tuple[int, int, int], input_list: list[str]) -> None:
        self.num_red = num_rgb[0]
        self.num_green = num_rgb[1]
        self.num_blue = num_rgb[2]
        self.input_list = input_list

    def is_game_possible(self, game: Game) -> bool:
        """
        Check if the game is possible.
        :param game: The game ot check.
        :return: True if the game is possible
        """
        return (self.num_red >= game.largest_values["red"]
                and self.num_green >= game.largest_values["green"]
                and self.num_blue >= game.largest_values["blue"])
