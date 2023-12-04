import logging
import re

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.cards = input_file

    @staticmethod
    def get_winning_numbers(card: str) -> list[int]:
        pattern = r"[ \d]+(?=\|)"
        return list(map(int, re.search(pattern, card).group().split()))

    @staticmethod
    def get_playable_numbers(card: str) -> list[int]:
        pattern = r"(?<=\|)[ \d]+"
        return list(map(int, re.search(pattern, card).group().split()))

    def puzzle_1(self) -> int:
        total = 0
        for card in self.cards:
            count = 0
            for winning_num in self.get_winning_numbers(card):
                for playable in self.get_playable_numbers(card):
                    if winning_num == playable:
                        # logger.debug(winning_num)
                        count += 1

            if count > 0:
                total += pow(2, count - 1)
            else:
                total += 0
            logger.debug(total)

        return total
