import logging

from src.Day10.part_1.pipe import Pipe, Direction

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file

    def find_start(self) -> tuple[int, int]:
        """
        Get the start as a pair or coordinates.
        :return: The coordinates in (x, y) form.
        """
        for y, row in enumerate(self.input_file):
            for x, char in enumerate(row):
                if char == 'S':
                    return x, y

    def pipe_neighbors(self, pipe: Pipe) -> dict[Direction, Pipe]:
        x, y = pipe.coordinates

        neighbors = {}

        # Get the pipes neighbors
        if y != 0:
            neighbors[Direction.NORTH] = Pipe(self.input_file[y - 1][x], (x, y - 1))

        if y != len(self.input_file) - 1:
            neighbors[Direction.SOUTH] = Pipe(self.input_file[y + 1][x], (x, y + 1))

        if x != len(self.input_file[y]) - 1:
            neighbors[Direction.EAST] = Pipe(self.input_file[y][x + 1], (x + 1, y))

        if x != 0:
            neighbors[Direction.WEST] = Pipe(self.input_file[y][x - 1], (x - 1, y))

        return neighbors

    def has_two_connections(self, pipe: Pipe) -> bool:
        connections = 0
        for direction, neighbor in self.pipe_neighbors(pipe).items():
            if pipe.is_connected(direction, neighbor):
                connections += 1

        return connections == 2

    def solution(self):
        pass
