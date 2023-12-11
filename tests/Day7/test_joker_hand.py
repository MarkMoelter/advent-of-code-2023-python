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
