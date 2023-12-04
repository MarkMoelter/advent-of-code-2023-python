import re

from Day3.Part1.number import Number
from Day3.Part1.symbol import Symbol


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._symbols = self.symbols
        self._numbers = self.numbers

    @property
    def symbols(self) -> list[Symbol]:
        """
        Get the symbols in the input file.
        :return: A list of symbols.
        """
        symbols = []
        for y_pos, line in enumerate(self.input_file):
            for match in re.finditer(r"[^\d.\n]+", line):
                symbols.append(Symbol(match.group(), match.span()[0], y_pos))
        return symbols

    @property
    def numbers(self) -> list[Number]:
        """
        Get the numbers in the input file.
        :return: A list of numbers.
        """
        numbers = []
        for y_pos, line in enumerate(self.input_file):
            for match in re.finditer(r"\d+", line):
                numbers.append(Number(int(match.group()), (match.span()[0], match.span()[1] - 1), y_pos))
        return numbers

    def puzzle_1(self) -> int:
        """
        Get the sum of all the part numbers in the engine schematic.
        :return: The sum of the part numbers.
        """
        total = 0
        for num in self._numbers:
            for symbol in self._symbols:
                near_symbol_vertically = num.y_pos - 1 <= symbol.y_pos <= num.y_pos + 1
                near_symbol_horizontally = num.x_span[0] - 1 <= symbol.x_pos <= num.x_span[1] + 1
                if near_symbol_horizontally and near_symbol_vertically:
                    total += num.value
        return total
