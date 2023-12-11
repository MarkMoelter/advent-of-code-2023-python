import unittest

from src.Day7.part_2 import JokerHand
from src.Day7.part_1 import HandType


class TestJokerHand(unittest.TestCase):
    def test_hand_type_AJJJJ_returns_five_of_a_kind(self):
        hand = "AJJJJ"

        result = JokerHand(hand)

        self.assertEqual(HandType.FIVE_OF_A_KIND, result)

    def test_hand_type_AAKKJ_returns_full_house(self):
        hand = "AAKKJ"

        result = JokerHand(hand)

        self.assertEqual(HandType.FULL_HOUSE, result)
