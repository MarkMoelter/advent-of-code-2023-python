import logging

from Day5.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: str) -> None:
        super().__init__(input_file)

    @property
    def seeds(self) -> list[range]:
        seed_values = super().seeds

        is_starting_number = True
        starting_number = 0
        seed_ranges = []
        for value in seed_values:
            if is_starting_number:
                starting_number = value
                is_starting_number = False
            else:
                seed_ranges.append(range(starting_number, starting_number + value))
                is_starting_number = True

        return seed_ranges

    def solution(self) -> int:
        sol = 0

        for r in self.seeds:
            for i in r:
                loc_val = self.transform_seed(i, 0)

                # Add first value to seed
                if sol == 0:
                    sol = loc_val
                # Add new min value if found
                elif sol > loc_val:
                    sol = loc_val
        return sol
