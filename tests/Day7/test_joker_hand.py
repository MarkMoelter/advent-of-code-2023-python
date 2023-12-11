import unittest

from src.Day7.part_1 import HandType
from src.Day7.part_2 import JokerHand


class TestJokerHand(unittest.TestCase):
    def test_hand_type_AJJJJ_returns_five_of_a_kind(self):
        hand = "AJJJJ"

        result = JokerHand(hand)

        self.assertEqual(HandType.FIVE_OF_A_KIND, result.hand_type)

    def test_hand_type_AAKKJ_returns_full_house(self):
        hand = "AAKKJ"

        result = JokerHand(hand)

        self.assertEqual(HandType.FULL_HOUSE, result.hand_type)

    def test_hand_type_T55J5_returns_four_of_a_kind(self):
        hand = "T55J5"

        result = JokerHand(hand)

        self.assertEqual(HandType.FOUR_OF_A_KIND, result.hand_type)

    def test_hand_type_KTJJT_returns_four_of_a_kind(self):
        hand = "KTJJT"

        result = JokerHand(hand)

        self.assertEqual(HandType.FOUR_OF_A_KIND, result.hand_type)

    def test_hand_type_KT2JT_returns_three_of_a_kind(self):
        hand = "KT2JT"

        result = JokerHand(hand)

        self.assertEqual(HandType.THREE_OF_A_KIND, result.hand_type)

    def test_hand_type_AKQJ3_returns_one_pair(self):
        hand = "AKQJ3"

        result = JokerHand(hand)

        self.assertEqual(HandType.ONE_PAIR, result.hand_type)

    def test_hand_type_JJJJJ_returns_five_of_a_kind(self):
        hand = "JJJJJ"

        result = JokerHand(hand)

        self.assertEqual(HandType.FIVE_OF_A_KIND, result.hand_type)

    def test_joker_value_is_1(self):
        hand = "JJJJK"

        result = JokerHand(hand)

        self.assertEqual(1, result.joker_value)

    def test_cards_as_nums_JJJJK_returns_1_1_1_1_13(self):
        hand = "JJJJK"

        result = JokerHand(hand)

        self.assertListEqual([1, 1, 1, 1, 13], result.cards_as_nums)
