import logging

from tqdm import tqdm

from Day5.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: str) -> None:
        super().__init__(input_file)

    @property
    def seeds(self) -> list[range]:
        seed_values = super().seeds

        starting_number = 0
        seed_ranges = []
        for i, value in enumerate(seed_values):
            if i % 2 == 0:
                starting_number = value
            else:
                seed_ranges.append(range(starting_number, starting_number + value))

        return seed_ranges

    def solution(self) -> int:
        sol = 0
        tseeds = tqdm(self.seeds, "Ranges", leave=True, position=0)

        for r in tseeds:
            tr = tqdm(r, f"Range {r} seeds ", leave=True, position=0)
            for i in tr:
                loc_val = self.transform_seed(i, 0)

                # Add first value to seed
                if sol == 0:
                    sol = loc_val
                # Add new min value if found
                elif sol > loc_val:
                    sol = loc_val
        return sol
