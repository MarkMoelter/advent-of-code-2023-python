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

    def test_types_to_hand_list_returns_dict(self):
        result = self.p1.types_to_hand_list

        self.assertIsInstance(result, dict)

    def test_types_to_hand_list_returns_2_three_of_a_kind_hands(self):
        result = self.p1.types_to_hand_list

        self.assertEqual(2, len(result[HandType.THREE_OF_A_KIND]))

    def test_types_to_hand_list_returns_2_two_pair_hands(self):
        result = self.p1.types_to_hand_list

        self.assertEqual(2, len(result[HandType.TWO_PAIR]))

    def test_types_to_hand_list_returns_1_one_pair_hand(self):
        result = self.p1.types_to_hand_list

        self.assertEqual(1, len(result[HandType.ONE_PAIR]))

    def test_sort_by_strength_returns_T55J5_QQQJA_in_that_order(self):
        result = [hand.cards for hand in self.p1.sort_by_strength()[HandType.THREE_OF_A_KIND]]

        self.assertListEqual(["T55J5", "QQQJA"], result)

    def test_sort_by_strength_input_A52AA_and_33263_returns_33263_then_A52AA(self):
        p1 = Part1(["A52AA 1", "33263 2"])

        result = [hand.cards for hand in p1.sort_by_strength()[HandType.THREE_OF_A_KIND]]

        self.assertListEqual(["33263", "A52AA"], result)

    def test_sorted_hands_test_input_returns_expected_order(self):
        result = [hand.cards for hand in self.p1.sorted_hands()]

        self.assertListEqual(["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"], result)

    def test_solution_returns_6440(self):
        result = self.p1.solution()

        self.assertEqual(6440, result)
