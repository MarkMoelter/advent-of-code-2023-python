import logging
import re

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self._seeds = self.seeds
        self.maps: dict[str, list[tuple[int, int, int]]] = {}

    @property
    def seeds(self) -> list[int]:
        """
        Get the seeds from the input file.
        :return: The list of seeds.
        """
        pattern = r"(?<=seeds: )[ \d]+"
        return list(map(int, re.search(pattern, self.input_file).group().split()))

    @staticmethod
    def map_src_to_dest(input_val: int, transformation_map: list[tuple[int, int, int]]) -> int:
        """
        Map the input value from the source to the destination.
        :param input_val: The value to map to the destination.
        :param transformation_map: The map between source and destination.
        :return: The destination position that it maps to.
        """
        for src, dest, _range in transformation_map:
            if input_val in range(src, src + _range):
                return input_val - src + dest
        return input_val
