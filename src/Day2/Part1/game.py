import re


class Game:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.game_id = self._game_id()
        self.largest_values = {
            "red": self._max_color_count("red"),
            "green": self._max_color_count("green"),
            "blue": self._max_color_count("blue")
        }

    def _game_id(self) -> int:
        """
        Get the game id from the input string.
        :return: The game id as an int.
        """
        # Matches the game id in Game ##:
        #                             ^^
        game_id_pattern = r"(?<=^Game )\d+(?=:)"
        return int(re.search(game_id_pattern, self.input_string).group())

    def _max_color_count(self, color: str) -> int:
        """
        Get the highest color value from the input string.
        :param color: The color to get the highest value for.
        :return: The highest color value
        """
        pattern = rf"\d+(?= {color})"
        return int(re.search(pattern, self.input_string).group())
