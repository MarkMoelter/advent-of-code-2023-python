import unittest

from src.Day9.part_1 import Part1
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        file_path = r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day9\test_input.txt"
        self.p1 = Part1(
            read_file_lines(file_path))

    def test_sequences_test_input_returns_list(self):
        result = self.p1.sequences

        self.assertIsInstance(result, list)

    def test_sequences_test_input_returns_list_of_lists(self):
        result = self.p1.sequences

        for sequence in result:
            self.assertIsInstance(sequence, list)

    def test_sequences_test_input_returns_list_of_lists_of_ints(self):
        result = self.p1.sequences  # list

        for sequence in result:  # list
            for val in sequence:  # int
                self.assertIsInstance(val, int)

    def test_sequences_test_input_returns_expected_list(self):
        result = self.p1.sequences

        expected = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45]
        ]

        self.assertListEqual(expected, result)

    def test_sequence_history_test_input_first_sequence_returns_dict(self):
        sequence = self.p1.sequences[0]

        result = self.p1.sequence_history(sequence)

        self.assertIsInstance(result, dict)

    def test_sequence_history_test_input_first_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[0]

        result = self.p1.sequence_history(sequence)

        expected = {0: [3, 3]}

        self.assertDictEqual(expected, result)

    def test_forecast_next_value_test_input_first_sequence_returns_21(self):
        sequence = self.p1.sequences[0]

        history = self.p1.sequence_history(sequence)

        result = self.p1.forecast_next_value(history)

        self.assertEqual(21, result)

    def test_sequence_history_test_input_second_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[1]

        result = self.p1.sequence_history(sequence)

        expected = {0: [6, 5, 4], 1: [1, 1]}

        self.assertDictEqual(expected, result)

    def test_forecast_next_value_test_input_second_sequence_returns_28(self):
        sequence = self.p1.sequences[1]

        history = self.p1.sequence_history(sequence)

        result = self.p1.forecast_next_value(history)

        self.assertEqual(28, result)

    def test_sequence_history_test_input_third_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[2]

        result = self.p1.sequence_history(sequence)

        expected = {0: [7, 6, 5], 1: [1, 1]}

        self.assertDictEqual(expected, result)

    def test_forecast_next_value_test_input_third_sequence_returns_68(self):
        sequence = self.p1.sequences[2]

        history = self.p1.sequence_history(sequence)

        result = self.p1.forecast_next_value(history)

        self.assertEqual(68, result)

    def test_solution_test_input_returns_114(self):
        result = self.p1.solution()

        self.assertEqual(114, result)
