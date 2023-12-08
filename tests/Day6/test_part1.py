import unittest
from src.Day6.part_1 import Part1
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Part1(read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day6\test_input.txt"))


    def test_get_faster_combos_returns_4(self):
        self.assertEqual(4, self.p1.get_faster_combos((7, 9)))

    def test_get_faster_combos_returns_8(self):
        self.assertEqual(8, self.p1.get_faster_combos((15, 40)))

    def test_get_faster_combos_returns_9(self):
        self.assertEqual(9, self.p1.get_faster_combos((30, 200)))

    def test_solution_returns_288(self):
        self.assertEqual(288, self.p1.solution())
