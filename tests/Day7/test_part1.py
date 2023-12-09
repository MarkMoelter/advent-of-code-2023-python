import unittest

from src.Day7.part_1 import HandType, Part1
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Part1(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day7\test_input.txt"))

    def test_get_hand_type_given_AAAAA_returns_five_of_a_kind_enum(self):
        hand = "AAAAA"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.FIVE_OF_A_KIND, result)

    def test_get_hand_type_given_AAAAK_returns_four_of_a_kind_enum(self):
        hand = "AAAAK"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.FOUR_OF_A_KIND, result)

    def test_get_hand_type_given_AAAKK_returns_full_house_enum(self):
        hand = "AAAKK"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.FULL_HOUSE, result)

    def test_get_hand_type_given_AAAKQ_returns_three_of_a_kind_enum(self):
        hand = "AAAKQ"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.THREE_OF_A_KIND, result)

    def test_get_hand_type_given_AAKKQ_returns_two_pair_enum(self):
        hand = "AAKKQ"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.TWO_PAIR, result)

    def test_get_hand_type_given_AAKQJ_returns_one_pair_enum(self):
        hand = "AAKQJ"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.ONE_PAIR, result)

    def test_get_hand_type_given_AKQJ9_returns_high_card_enum(self):
        hand = "AKQJ9"

        result = self.p1.get_hand_type(hand)

        self.assertEqual(HandType.HIGH_CARD, result)
