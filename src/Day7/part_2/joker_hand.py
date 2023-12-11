from collections import Counter

from src.Day7.part_1 import Hand, HandType


class JokerHand(Hand):
    def __init__(self, cards: str, bid: int = 1) -> None:
        self.joker_value = 1
        super().__init__(cards, bid)
        self._cards_as_nums = self.cards_as_nums

    @property
    def cards_as_nums(self) -> list[int]:
        """
        Convert the hand to a list of integers corresponding the strength of the card.
        :return: A list representing the cards as strengths.
        """
        return [self.joker_value
                if card == 11
                else card
                for card in super().cards_as_nums
                ]

    @property
    def hand_type(self) -> HandType:
        """
        Get the type of the hand.
        If there is not a joker in the hand, will return part1 implementation.

        Caveats:

        - If there is a joker in the hand, cannot return high card or two pair.
        - It will jump from high card to one pair or jump straight to three of a kind for multiple jokers.

        :return: The type of the hand.
        """
        # If no joker
        if "J" not in self.cards:
            return super().hand_type

        # Edge case as loop ignores joker
        if self.cards == "JJJJJ":
            return HandType.FIVE_OF_A_KIND

        hand_count = Counter(self._cards_as_nums)
        # Get the card with the highest count; If count tie, take stronger card
        max_card, max_count = 0, 0
        for card, count in hand_count.items():
            # Ignore Jokers
            if card == self.joker_value:
                continue
            if count > max_count:
                max_card, max_count = card, count

        hand_count[max_card] += hand_count.pop(self.joker_value)

        if 5 in hand_count.values():
            return HandType.FIVE_OF_A_KIND
        if 4 in hand_count.values():
            return HandType.FOUR_OF_A_KIND
        if 3 in hand_count.values() and 2 in hand_count.values():
            return HandType.FULL_HOUSE
        if 3 in hand_count.values():
            return HandType.THREE_OF_A_KIND
        return HandType.ONE_PAIR

    def __str__(self) -> str:
        return f"{super().__str__()}; {self.letter_to_int}, {self._cards_as_nums}"
