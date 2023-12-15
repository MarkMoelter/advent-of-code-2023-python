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

        result = self.p1.sequence_history({0: sequence[::-1]})

        self.assertIsInstance(result, dict)

    def test_sequence_history_test_input_first_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[0]

        result = self.p1.sequence_history({0: sequence[::-1]})

        expected = {0: sequence[::-1], 1: [3, 3]}

        self.assertDictEqual(expected, result)

    def test_sequence_history_test_input_second_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[1]

        result = self.p1.sequence_history({0: sequence[::-1]})

        expected = {0: sequence[::-1], 1: [6, 5, 4, 3, 2], 2: [1, 1]}

        self.assertDictEqual(expected, result)

    def test_sequence_history_test_input_third_sequence_returns_expected_history(self):
        sequence = self.p1.sequences[2]

        result = self.p1.sequence_history({0: sequence[::-1]})

        expected = {0: sequence[::-1], 1: [15, 9, 5, 3, 3], 2: [6, 4, 2, 0], 3: [2, 2]}

        self.assertDictEqual(expected, result)

    def test_forecast_next_value_test_input_returns_int(self):
        sequence = self.p1.sequences[0]

        result = self.p1.forecast_next_value(sequence)

        self.assertIsInstance(result, int)

    def test_forecast_next_value_test_input_first_sequence_returns_18(self):
        sequence = self.p1.sequences[0]

        result = self.p1.forecast_next_value(sequence)

        self.assertEqual(18, result)

    def test_forecast_next_value_test_input_second_sequence_returns_28(self):
        sequence = self.p1.sequences[1]

        result = self.p1.forecast_next_value(sequence)

        self.assertEqual(28, result)

    def test_forecast_next_value_test_input_third_sequence_returns_68(self):
        sequence = self.p1.sequences[2]

        result = self.p1.forecast_next_value(sequence)

        self.assertEqual(68, result)

    def test_solution_test_input_returns_114(self):
        result = self.p1.solution()

        self.assertEqual(114, result)
