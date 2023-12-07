import logging
import re

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self._seeds = self.seeds
        self._maps: dict[str, list[tuple[int, int, int]]] = self.maps
        self.int_to_map: dict[int, str] = {
            i: ele for i, ele in
            enumerate([
                "seed_soil",
                "soil_fertilizer",
                "fertilizer_water",
                "water_light",
                "light_temperature",
                "temperature_humidity",
                "humidity_location"
            ])
        }

    @property
    def seeds(self) -> list[int]:
        """
        Get the seeds from the input file.
        :return: The list of seeds.
        """
        pattern = r"(?<=seeds: )[ \d]+"
        return list(map(int, re.search(pattern, self.input_file).group().split()))

    @property
    def maps(self) -> dict[str, list[tuple[int, int, int]]]:

        # Split each map based on the double newlines found at the end of each map
        split_maps = re.split(r"\n\n", self.input_file)
        split_maps.pop(0)  # remove seeds as it is not a map

        sol = {}
        for _map in split_maps:
            # Get the map name
            map_name = re.search(r".*(?= map:)", _map).group().replace("-to-", "_")

            # Get the values from the input file; Always 3 numbers, split apart, convert to int and store as list[tuple]
            map_values = [tuple(map(int, i)) for i in map(str.split, re.findall(r"\d+ \d+ \d+", _map))]
            sol[map_name] = map_values  # Add name and values to the dict
        return sol

    @staticmethod
    def map_src_to_dest(input_val: int, transformation_map: list[tuple[int, int, int]]) -> int:
        """
        Map the input value from the source to the destination.
        :param input_val: The value to map to the destination.
        :param transformation_map: The map between source and destination.
        :return: The destination position that it maps to.
        """
        for dest, src, _range in transformation_map:
            if input_val in range(src, src + _range):
                return input_val - src + dest
        return input_val

    def transform_seed(self, val: int, map_number: int) -> int:
        """
        Recursively find the transformations from seed to location.
        :param val: The initial value that needs to be transformed.
        :param map_number: The index the map to use.
        :return: The location of the seed.
        """
        if map_number == len(self._maps):
            return val

        transformed_val = self.map_src_to_dest(val, self._maps[self.int_to_map[map_number]])
        logger.debug(f"Value: {val}; Using map: {self.int_to_map[map_number]}; Transformed value: {transformed_val}")
        return self.transform_seed(transformed_val, map_number + 1)

    def solution(self) -> int:
        """
        Solution to the first problem
        :return: The lowest location that corresponds to any of the initial seeds.
        """
        sol = {}
        for seed in self._seeds:
            sol[seed] = self.transform_seed(seed, 0)

        return min(sol.values())
