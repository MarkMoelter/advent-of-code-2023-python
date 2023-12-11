from Day7.part_1 import HandType
from src.Day7.part_1 import Hand


class JokerHand(Hand):
    def __init__(self, cards: str, bid: int = 1) -> None:
        super().__init__(cards, bid)
        self.letter_to_int["J"] = 1

    @property
    def hand_type(self) -> HandType:
        return super().hand_type




