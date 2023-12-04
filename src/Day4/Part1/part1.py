import logging

from Day4.Part1.card import Card

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self._input_file = input_file
        self._cards = self.cards

    @property
    def cards(self) -> list[Card]:
        return [Card(card) for card in self._input_file]

    def puzzle_1(self) -> int:
        total = 0
        for card in self._cards:
            count = 0
            for winning_num in card.winning_numbers:
                for playable in card.playable_numbers:
                    if winning_num == playable:
                        count += 1

            if count > 0:
                total += pow(2, count - 1)
            else:
                total += 0
            logger.debug(total)

        return total
