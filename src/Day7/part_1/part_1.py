import logging

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._hands = self.hands

    @property
    def hands(self) -> list[tuple[str, int]]:
        out = []
        for line in self.input_file:
            hand, bid = line.split()
            out.append((hand, int(bid)))

        return out

    def solution(self):
        out = 0

        for hand in self._hands:
            pass

        return out
