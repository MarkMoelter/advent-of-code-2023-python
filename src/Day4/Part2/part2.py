import logging

from Day4.Part1.card import Card
from Day4.Part1.part1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)
        self.cache = dict()

    def puzzle_2(self) -> int:
        total = 0
        for card in self.cards:
            logger.debug(f"Original card: {card.card_id}")
            total += self.get_number_of_cards_generated(card)
            logger.debug(f"Running total: {total}\n")
            logger.debug(f"Final cache: {self.cache}")

        return total

    def get_number_of_cards_generated(self, card: Card) -> int:
        """
        Get the total number of cards generated for puzzle 2.
        :param card: The initial card, also the top node in the tree.
        :return: The number of cards generated.
        """
        # Check if the node has already been cached
        if card.card_id in self.cache:
            cached_count = self.cache[card.card_id]
            logger.debug(f"Using cache for card: {card.card_id}. Cached count: {cached_count}")
            return cached_count

        # Check if the card is at the bottom of the tree
        logger.debug(f"Card not cached, ID: {card.card_id} -> {card.numbers_that_won}")
        if len(card.numbers_that_won) == 0:
            self.cache[card.card_id] = 1
            return 1

        # Iterate through all children of the node
        count = 1
        for card2 in self.cards[card.card_id: card.card_id + len(card.numbers_that_won)]:
            count += self.get_number_of_cards_generated(card2)

        if card.card_id not in self.cache:
            self.cache[card.card_id] = count

        return count
