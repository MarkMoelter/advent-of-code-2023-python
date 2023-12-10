import unittest

from src.Day7.part_1 import Hand, HandType


class TestHand(unittest.TestCase):
    def test_card_as_nums_AAAAA_returns_14_14_14_14_14(self):
        hand = Hand("AAAAA")

        result = hand.cards_as_nums

        self.assertEqual([14, 14, 14, 14, 14], result)

    def test_card_as_nums_A68TJ_returns_14_6_8_10_11(self):
        hand = Hand("A68TJ")

        result = hand.cards_as_nums

        self.assertEqual([14, 6, 8, 10, 11], result)

    def test_hand_type_given_AAAAA_returns_five_of_a_kind_enum(self):
        hand = Hand("AAAAA")

        result = hand.hand_type

        self.assertEqual(HandType.FIVE_OF_A_KIND, result)

    def test_hand_type_given_AAAAK_returns_four_of_a_kind_enum(self):
        hand = Hand("AAAAK")

        result = hand.hand_type

        self.assertEqual(HandType.FOUR_OF_A_KIND, result)

    def test_hand_type_given_AAAKK_returns_full_house_enum(self):
        hand = Hand("AAAKK")

        result = hand.hand_type

        self.assertEqual(HandType.FULL_HOUSE, result)

    def test_hand_type_given_AAAKQ_returns_three_of_a_kind_enum(self):
        hand = Hand("AAAKQ")

        result = hand.hand_type

        self.assertEqual(HandType.THREE_OF_A_KIND, result)

    def test_hand_type_given_AAKKQ_returns_two_pair_enum(self):
        hand = Hand("AAKKQ")

        result = hand.hand_type

        self.assertEqual(HandType.TWO_PAIR, result)

    def test_hand_type_given_AAKQJ_returns_one_pair_enum(self):
        hand = Hand("AAKQJ")

        result = hand.hand_type

        self.assertEqual(HandType.ONE_PAIR, result)

    def test_hand_type_given_AKQJ9_returns_high_card_enum(self):
        hand = Hand("AKQJ9")

        result = hand.hand_type

        self.assertEqual(HandType.HIGH_CARD, result)
