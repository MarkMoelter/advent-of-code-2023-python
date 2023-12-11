from collections import Counter

from .hand_type import HandType


class Hand:
    def __init__(self, cards: str, bid: int = 1) -> None:
        self.cards = cards
        self.bid = bid
        self.letter_to_int = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self._cards_as_nums = self.cards_as_nums
        self._hand_type = self.hand_type

    @property
    def cards_as_nums(self) -> list[int]:
        """
        Convert all alphabetical cards to their corresponding numerical value.
        :return: A list of cards with corresponding numbers in the place of letters.
        """
        out = []
        for card in self.cards:
            if card.isalpha():
                out.append(self.letter_to_int[card])
            else:
                out.append(int(card))

        return out

    @property
    def hand_type(self) -> HandType:
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
        :return: The type of the hand.
        """
        char_to_count = Counter(self._cards_as_nums)
        if 5 in char_to_count.values():
            return HandType.FIVE_OF_A_KIND
        if 4 in char_to_count.values():
            return HandType.FOUR_OF_A_KIND
        if 3 in char_to_count.values() and 2 in char_to_count.values():
            return HandType.FULL_HOUSE
        if 3 in char_to_count.values():
            return HandType.THREE_OF_A_KIND
        if len(set(self.cards)) == 3:
            return HandType.TWO_PAIR
        if len(set(self.cards)) == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __str__(self) -> str:
        return f"{self.__class__}({self.cards}, {self.bid}, {self.hand_type})"
