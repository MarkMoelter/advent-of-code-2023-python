import logging
from collections import Counter

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._sequences = self.sequences

    @property
    def sequences(self) -> list[list[int]]:
        """
        Get the individual sequences from the input file.
        :return: The input sequences as a list of sequences.
        """
        out = []
        for line in self.input_file:
            out.append(list(map(int, line.split())))

        return out

    def sequence_history(self, sequence_history: dict[int, list[int]], layer: int = 0) -> dict[int, list[int]]:
        """
        Extrapolate the history of the sequence starting from the end.
        Reverses the sequence to avoid getting all values in the sequence, using only the required data.
        :param sequence_history: The sequence to extract the history from.
        :param layer: The current layer of the sequence.
        :return:A dictionary with a list per sequence layer.
        """
        sequence_history[layer + 1] = []
        layer_list = sequence_history[layer]
        for i, num in enumerate(layer_list):
            # recursive end condition
            if len(Counter(sequence_history[layer + 1])) == 1 and i > 1:
                return sequence_history

            # end of list
            if i + 1 == len(layer_list):
                break

            diff = layer_list[i] - layer_list[i + 1]
            sequence_history[layer + 1].append(diff)

        return self.sequence_history(sequence_history, layer + 1)

    def forecast_next_value(self, sequence: list[int]) -> int:
        """
        Extrapolate the history of the sequence starting from the end.
        Reverses the sequence to avoid getting all values in the sequence, using only the required data.
        :param sequence: The sequence to extract the history from.
        :return: The next value in the sequence.
        """

        # Take the first value from each layer in the sequence. Sums to the next value.
        out = 0
        sequence_history = self.sequence_history({0: sequence[::-1]}, 0)
        for layer in sequence_history.values():
            out += layer[0]

        return out

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
