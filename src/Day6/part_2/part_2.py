import logging

from src.Day6.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)
        self._race = self.race

    @property
    def race(self) -> tuple[int, int]:
        out = []
        for line in self.input_file:
            line = line.split()
            line.pop(0)
            out.append(int(''.join(line)))

        return out[0], out[1]

    def solution(self) -> int:
        return self.get_faster_combos(self._race)
