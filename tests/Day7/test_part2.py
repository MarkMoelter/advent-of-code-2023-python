import unittest

from src.Day7.part_2 import Part2
from src.read_file import read_file_lines


class TestPart2(unittest.TestCase):
    def setUp(self) -> None:
        self.p2 = Part2(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day7\test_input.txt"))

    def test_solution_returns_5905(self):
        result = self.p2.solution()

        self.assertEqual(5905, result)
