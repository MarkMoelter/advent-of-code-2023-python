import logging

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._races = self.races

    @property
    def races(self) -> list[tuple[int, int]]:
        out = []
        for line in self.input_file:
            line = line.split()
            line.pop(0)
            out.append(list(map(int, line)))

        return [i for i in zip(out[0], out[1])]

    def solution(self) -> int:
        out = 1
        for race in self._races:
            out *= self.get_faster_combos(race)
        return out

    @staticmethod
    def get_faster_combos(race: tuple[int, int]) -> int:
        """
        Get the combinations in the race that are faster than the current record.
        :param race: The race made up of the time and the current record.
        :return: The combinations that are faster than the current record
        """
        faster_combos = 0
        time, record = race

        # Only deal with the first half of the time. It repeats in the second half.
        for i in range(time // 2 + 1):
            if (time - i) * i > record:
                faster_combos += 1

        # Multiply the result by 2 to account for only using the first half
        faster_combos *= 2

        # Even numbers will have 1 extra combo after multiplying. Subtract 1 to account for
        if time % 2 == 0:
            faster_combos -= 1

        return faster_combos
