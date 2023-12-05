import logging

from Day4.Part1.card import Card
from Day4.Part1.part1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)

    def puzzle_2(self) -> int:
        total = 0
        for card in self.cards:
            logger.debug(f"Original card: {card.card_id}")
            total += self.get_ticket_count(card, 0)
            logger.debug(f"Running total: {total}\n")

        return total

    def get_ticket_count(self, card: Card, count: int) -> int:
        """
        Get the number of cards generated from the cards winnings
        :param count: The running total.
        :param card: The card.
        :return: The number of cards generated from the cards winnings.
        """
        count += 1
        logger.debug(f" -> ID: {card.card_id} -> {card.numbers_that_won} -> Count: {count}")
        if len(card.numbers_that_won) == 0:
            return count

        for card2 in self.cards[card.card_id: card.card_id + len(card.numbers_that_won)]:
            count = self.get_ticket_count(card2, count)

        return count
