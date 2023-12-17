import logging

from template.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)
