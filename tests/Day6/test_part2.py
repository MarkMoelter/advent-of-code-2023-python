import unittest

from src.Day6.part_2 import Part2
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.p2 = Part2(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day6\test_input.txt"))

    def test_race_returns_tuple(self):
        self.assertIsInstance(self.p2.race, tuple)

    def test_race_returns_test_input_correct(self):
        self.assertEqual(self.p2.race, (71530, 940200))

    def test_solution_returns_71503(self):
        self.assertEqual(71503, self.p2.solution())
