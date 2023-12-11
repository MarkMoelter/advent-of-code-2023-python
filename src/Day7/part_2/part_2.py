import logging

from src.Day7.part_1 import Part1, Hand
from src.Day7.part_2.joker_hand import JokerHand

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)

    @property
    def hands(self) -> list[Hand]:
        return [JokerHand(hand.cards, hand.bid)
                for hand in super().hands]
