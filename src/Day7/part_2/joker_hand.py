from Day7.part_1 import HandType
from src.Day7.part_1 import Hand


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
        return super().hand_type




