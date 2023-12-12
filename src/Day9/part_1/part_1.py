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

    def sequence_history(self, sequence: list[int]) -> dict[int, list[int]]:
        """
        Extrapolate the history of the sequence starting from the end.
        Reverses the sequence to avoid getting all values in the sequence, using only the required data.
        :param sequence: The sequence to extract the history from.
        :return:A dictionary with a list per sequence layer.
        """

    def forecast_next_value(self, sequence_history: dict[int, list[int]]) -> int:
        """
        Forecast the next value in the sequence.
        :param sequence_history: The history of the sequence as a dictionary with a list per sequence layer.
        :return: The next value in the sequence.
        """

    def solution(self) -> int:
        """
        Get the sum of the forecasted value in each sequence.
        :return: The sum of the forecasted values.
        """
        out = 0
        for seq in self._sequences:
            history = self.sequence_history(seq)
            out += self.forecast_next_value(history)

        return out
