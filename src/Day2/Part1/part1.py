import logging
import math

from Day2.Part1.game import Game

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_list: list[str]) -> None:
        self.input_list = input_list

    @staticmethod
    def is_game_possible(game: Game, num_rgb: tuple[int, int, int], ) -> bool:
        """
        Check if the game is possible.
        :param game: The game ot check.
        :param num_rgb:
        :return: True if the game is possible.
        """

        num_red = num_rgb[0]
        num_green = num_rgb[1]
        num_blue = num_rgb[2]

        return (num_red >= max(game.rgb_values["red"])
                and num_green >= max(game.rgb_values["green"])
                and num_blue >= max(game.rgb_values["blue"]))

    @staticmethod
    def fewest_cubes_needed(game: Game) -> tuple[int, int, int]:
        """
        Get the fewest cubes needed for each game. Return tuple as RGB values.
        :param game: The game to analyze.
        :return: The fewest cubes needed for each game as RGB values.
        """

        red = max(game.rgb_values["red"])
        green = max(game.rgb_values["green"])
        blue = max(game.rgb_values["blue"])

        return red, green, blue

    def add_game_ids_of_possible_games(self, rgb_values: tuple[int, int, int]) -> int:
        """
        Add the ids of the possible games.
        :return: The first puzzle's answer.
        """
        total = 0
        for line in self.input_list:
            game = Game(line)
            if self.is_game_possible(game, rgb_values):
                total += game.game_id

        return total

    def sum_of_powers_of_lowest_needed_cubes(self) -> int:
        """
        Sum the powers of the fewest needed cubes in each game.
        :return: The second puzzle's answer.
        """
        total = 0
        for idx, line in enumerate(self.input_list):
            game = Game(line)
            fewest = self.fewest_cubes_needed(game)
            mul = math.prod(fewest)
            logger.debug(f"{idx + 1}: {fewest} = {mul}")
            total += mul

        return total
