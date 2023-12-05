import re


class Card:
    def __init__(self, card_string: str) -> None:
        self._card_string = card_string
        self._card_id = self.card_id
        self._winning_numbers = self.winning_numbers
        self._playable_numbers = self.playable_numbers
        self._numbers_that_won = self.numbers_that_won

    @property
    def card_id(self) -> int:
        """
        Get the card id from the card.
        :return: The card id.
        """
        pattern = r"\d+(?=:)"
        return int(re.search(pattern, self._card_string).group())

    @property
    def winning_numbers(self) -> list[int]:
        """
        Get the winning numbers.
        :return: A list of the winning numbers.
        """
        pattern = r"[ \d]+(?=\|)"
        return list(map(int, re.search(pattern, self._card_string).group().split()))

    @property
    def playable_numbers(self) -> list[int]:
        """
        Get the playable numbers.
        :return: A list of the playable numbers.
        """
        pattern = r"(?<=\|)[ \d]+"
        return list(map(int, re.search(pattern, self._card_string).group().split()))

    @property
    def numbers_that_won(self) -> list[int]:
        """
        Get the numbers that won on the card.
        :return: A list of the numbers that won on the card.
        """
        return [
            winning
            for winning in self._winning_numbers
            for playable in self._playable_numbers
            if winning == playable
        ]
