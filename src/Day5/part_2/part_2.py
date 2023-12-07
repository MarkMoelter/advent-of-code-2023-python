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
        if self.load("state.txt"):
            load_idx, sol = self.load("state.txt")
            logger.info(f"Using saved values: {load_idx} {sol}")
        else:
            load_idx = -1
            sol = 0
        logger.debug(f"{load_idx} {sol}")

        for idx, r in enumerate(self.seeds):
            if load_idx >= idx:
                continue
            for i in tqdm(r, f"Calculate seed locations", leave=True, position=0):
                loc_val = self.transform_seed(i, 0)

                # Add first value to seed
                if sol == 0:
                    sol = loc_val
                # Add new min value if found
                elif sol > loc_val:
                    sol = loc_val

            self.save("state.txt", idx, sol)
            logger.info(f"Saved Values: {self.load("state.txt")}")
        return sol

    @staticmethod
    def save(filename: str, idx: int, current_smallest: int):
        with open(filename, "w+") as f:
            f.write(f"{idx} {current_smallest}")

    @staticmethod
    def load(filename: str) -> tuple[int, ...]:
        with open(filename, "r") as f:
            return tuple(map(int, f.read().split()))
