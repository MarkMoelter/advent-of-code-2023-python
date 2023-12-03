import re


class Game:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.game_id = self._game_id()
        self.rgb_values: dict[str, list[int]] = {
            "red": self._color_count_all_rounds("red"),
            "green": self._color_count_all_rounds("green"),
            "blue": self._color_count_all_rounds("blue")
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

    def _color_count_all_rounds(self, color: str) -> list[int]:
        """
        Get all values of a single color from the input string.
        :param color: The color to search for
        :return: The values for the color parameter.
        """
        pattern = rf"\d+(?= {color})"
        return list(map(int, re.findall(pattern, self.input_string)))
