import unittest

from src.Day7.part_1 import Part1, Hand, HandType
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Part1(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day7\test_input.txt"))

    def test_hands_prop_test_input_returns_list(self):
        result = self.p1.hands

        self.assertIsInstance(result, list)

    def test_hands_prop_test_input_returns_list_of_hand(self):
        result = self.p1.hands

        for hand in result:
            self.assertIsInstance(hand, Hand)

    def test_hand_prop_test_input_returns_len_5(self):
        result = self.p1.hands

        self.assertEqual(5, len(result))

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

    def test_sort_hands_by_type_returns_one_vali_in_high_card_list(self):
        hand_bet = "AKQJ9 7"

        result = Part1([hand_bet]).sort_hands_by_type()

        self.assertEqual(1, len(result[HandType.HIGH_CARD]))
