import unittest

from src.Day7.part_1 import HandType, Part1
from src.read_file import read_file_lines


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Part1(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day7\test_input.txt"))

    def test_get_hand_type_given_AAAAA_returns_five_of_a_kind_enum(self):
        hand = "AAAAA"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.FIVE_OF_A_KIND, result)
