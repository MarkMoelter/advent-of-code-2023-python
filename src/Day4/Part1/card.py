import re


class Card:
    def __init__(self, card_string: str) -> None:
        self._card_string = card_string
        self._card_id = self.card_id
        self._winning_numbers = self.winning_numbers
        self._playable_numbers = self.playable_numbers

    @property
    def card_id(self) -> int:
        pattern = r"\d+(?=:)"
        return int(re.search(pattern, self._card_string).group())

    @property
    def winning_numbers(self) -> list[int]:
        pattern = r"[ \d]+(?=\|)"
        return list(map(int, re.search(pattern, self._card_string).group().split()))

    @property
    def playable_numbers(self) -> list[int]:
        pattern = r"(?<=\|)[ \d]+"
        return list(map(int, re.search(pattern, self._card_string).group().split()))
