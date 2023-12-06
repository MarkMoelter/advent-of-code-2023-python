import logging

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_input: list[str]) -> None:
        self.input_input = input_input

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
