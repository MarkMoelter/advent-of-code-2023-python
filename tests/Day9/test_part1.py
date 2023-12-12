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

    def test_sequences_test_input_returns_correct_list(self):
        result = self.p1.sequences

        expected = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45]
        ]

        self.assertListEqual(expected, result)
