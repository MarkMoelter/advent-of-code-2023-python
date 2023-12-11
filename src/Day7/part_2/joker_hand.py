from collections import Counter

from src.Day7.part_1 import Hand, HandType


class JokerHand(Hand):
    def __init__(self, cards: str, bid: int = 1) -> None:
        self.joker_value = 1
        super().__init__(cards, bid)
        self._cards_as_nums = self.cards_as_nums

    @property
    def cards_as_nums(self) -> list[int]:
        return [self.joker_value
                if card == 11
                else card
                for card in super().cards_as_nums
                ]

    @property
    def hand_type(self) -> HandType:
        if "J" not in self.cards:
            return super().hand_type
        if self.cards == "JJJJJ":
            return HandType.FIVE_OF_A_KIND

        hand_count = Counter(self._cards_as_nums)

        # Get the card with the highest count
        max_card, max_count = 0, 0
        for card, count in hand_count.items():
            if card == self.joker_value:
                continue
            if count > max_count:
                max_card, max_count = card, count

        hand_count[max_card] += hand_count[self.joker_value]

        if 5 in hand_count.values():
            return HandType.FIVE_OF_A_KIND
        if 4 in hand_count.values():
            return HandType.FOUR_OF_A_KIND
        if 3 in hand_count.values() and 2 in hand_count.values():
            return HandType.FULL_HOUSE
        if 3 in hand_count.values():
            return HandType.THREE_OF_A_KIND
        if len(set(self.cards)) == 3:
            return HandType.TWO_PAIR
        if len(set(self.cards)) == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __str__(self) -> str:
        return f"{super().__str__()}; {self.letter_to_int}, {self._cards_as_nums}"
