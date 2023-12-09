import logging

from .hand_type import HandType
from collections import Counter

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._hands = self.hands

    @property
    def hands(self) -> list[tuple[str, int]]:
        """
        Get a list of hands and bids from the input file.
        :return: The list of hands.
        """
        out = []
        for line in self.input_file:
            hand, bid = line.split()
            out.append((hand, int(bid)))

        return out

    @staticmethod
    def get_hand_type(hand: str) -> HandType:
        """
        Get the type of the hand.

        Possible types:

        - five of a kind
        - Four of a kind
        - Full house
        - Three of a kind
        - Two pair
        - One pair
        - High card
        :param hand: Consists of 5 cards.
        :return: The type of the hand.
        """
        char_to_count = Counter(hand)
        if 5 in char_to_count.values():
            return HandType.FIVE_OF_A_KIND
        if 4 in char_to_count.values():
            return HandType.FOUR_OF_A_KIND
        if 3 in char_to_count.values() and 2 in char_to_count.values():
            return HandType.FULL_HOUSE
        if 3 in char_to_count.values():
            return HandType.THREE_OF_A_KIND
        if len(set(hand)) == 3:
            return HandType.TWO_PAIR
        if len(set(hand)) == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def sort_hands_by_type(self) -> dict[HandType, list[tuple[str, int]]]:
        """
        Sort hands into their respective hand types.
        :return: A dict of hand types and their corresponding hands.
        """
        pass

    def sort_hands_by_strength(self, hands: list[tuple[str, int]]) -> list[tuple[str, int]]:
        """
        Sort the list of hands by their strength from worst to best.
        :param hands: The list of hands to sort.
        :return: The list of hands sorted by their strength.
        """

    def sorted_hands(self) -> list[tuple[str, int]]:
        """
        Sort hands within each hand type and return all hands sorted from worst to best.
        :return:
        """
        out = []
        for hand_type in HandType:
            out.extend(self.sort_hands_by_strength(self.sort_hands_by_type()[hand_type]))
        return out

    def solution(self) -> int:
        out = 0

        for idx, _, bid in enumerate(self.sorted_hands()):
            strength = idx + 1
            out += bid * strength
        return out
