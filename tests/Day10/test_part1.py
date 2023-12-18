import unittest

from src.Day10.part_1 import Part1
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        file_path = r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day10\test_input.txt"
        self.p1 = Part1(
            read_file_lines(file_path))

    @unittest.skip("Method not implemented")
    def test_solution_test_input_returns_8(self):
        result = self.p1.solution()

        self.assertEqual(8, result)
