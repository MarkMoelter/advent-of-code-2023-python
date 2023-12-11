import unittest

from src.Day7.part_2 import Part2, JokerHand
from src.read_file import read_file_lines


class TestPart2(unittest.TestCase):
    def setUp(self) -> None:
        self.p2 = Part2(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day7\test_input.txt"))

    def test_solution_returns_5905(self):
        result = self.p2.solution()

        self.assertEqual(5905, result)

    def test_sorted_hands_returns_correct_order(self):
        result = [hand.cards for hand in self.p2.sorted_hands()]

        self.assertListEqual(["32T3K", "KK677", "T55J5", "QQQJA", "KTJJT"], result)

    def test_hands_property_returns_list_of_joker_hands(self):
        result = self.p2.hands

        for val in result:
            self.assertIsInstance(val, JokerHand)
