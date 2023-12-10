import logging

from .hand import Hand
from .hand_type import HandType

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._hands = self.hands
        self._types_to_hand_list = self.types_to_hand_list

    @property
    def hands(self) -> list[Hand]:
        """
        Get a list of hands and bids from the input file.
        :return: The list of hands.
        """
        out = []
        for line in self.input_file:
            cards, bid = line.split()
            out.append(Hand(cards, int(bid)))
        return out

    @property
    def types_to_hand_list(self) -> dict[HandType, list[Hand]]:
        """
        Sort hands into their respective hand types.
        :return: A dict of hand types and their corresponding hands.
        """
        out = {hand_type: [] for hand_type in HandType}
        for hand in self._hands:
            out[hand.hand_type].append(hand)
        return out

    def sort_by_strength(self) -> None:
        """
        Sort the list of hands by their strength from worst to best.
        :return: The list of hands sorted by their strength.
        """

        for hand_type, hand_list in self._types_to_hand_list:
            decorated = [(hand.cards_as_nums, hand) for hand in hand_list]
            decorated.sort()
            self._types_to_hand_list[hand_type] = [hand for (cards, hand) in decorated]

    def sorted_hands(self) -> list[Hand]:
        """
        Sort hands within each hand type and return all hands sorted from worst to best.
        :return:
        """
        out = []
        for hand_type in HandType:
            out.extend(self._types_to_hand_list[hand_type])
        return out

    def solution(self) -> int:
        out = 0
        for idx, hand in enumerate(self.sorted_hands()):
            strength = idx + 1
            out += hand.bid * strength
        return out
