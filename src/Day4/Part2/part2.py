import logging

from Day4.Part1.card import Card
from Day4.Part1.part1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)
        self.counter = 0

    def puzzle_2(self) -> int:
        total = 0
        total += self.get_ticket_count(self.cards[3], 0)
        return total

    def get_ticket_count(self, card: Card, total: int) -> int:
        """
        Get the number of cards generated from the cards winnings
        :param total: The running total.
        :param card: The card.
        :return: The number of cards generated from the cards winnings.
        """
        logger.debug(f" -> ID: {card.card_id} -> {card.numbers_that_won}")

        # Account for the card
        total += 1

        if card.card_id == len(self.cards):
            return 1
        elif len(card.numbers_that_won) == 0:
            return 1

        total += len(card.numbers_that_won)
        return self.get_ticket_count(self.cards[card.card_id], total) + total
