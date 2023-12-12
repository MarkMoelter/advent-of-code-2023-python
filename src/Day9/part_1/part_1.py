import logging

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._sequences = self.sequences

    @property
    def sequences(self) -> list[list[int]]:
        out = []
        for line in self.input_file:
            out.append(list(map(int, line.split())))

        return out

    def forecast_next_value(self, sequence: list[int]) -> int:
        """
        Forecast the next value in the sequence.
        :param sequence: The sequence to forecast the next value in.
        :return: The next value in the sequence.
        """

    def solution(self) -> int:
        """
        Get the sum of the next value in each sequence.
        :return: The sum of the forecasted values.
        """
        out = 0
        for seq in self._sequences:
            out += self.forecast_next_value(seq)

        return out
