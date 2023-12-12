import unittest

from src.Day8.part_2 import Part2
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        file_path = r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day8\test_input_part_2.txt"
        self.p2 = Part2(
            read_file_lines(file_path))

    def test_naive_solution_test_input_returns_6(self):
        result = self.p2.naive_solution("A", "Z")

        self.assertEqual(6, result)

    def test_lcm_solution_test_input_returns_6(self):
        result = self.p2.lcm_solution("A", "Z")

        self.assertEqual(6, result)
