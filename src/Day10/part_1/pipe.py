from typing import Self

from src.Day10.part_1.direction import Direction


class Pipe:
    connections = {
        "|": {Direction.NORTH, Direction.SOUTH},
        "-": {Direction.EAST, Direction.WEST},
        "L": {Direction.NORTH, Direction.EAST},
        "J": {Direction.NORTH, Direction.WEST},
        "7": {Direction.SOUTH, Direction.WEST},
        "F": {Direction.SOUTH, Direction.EAST},
        "S": {Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST},
        ".": {}
    }

    def __init__(self, character: str, coordinates: tuple[int, int]) -> None:
        self.character = character
        self.coordinates = coordinates

    def is_connected(self, direction: Direction, pipe: Self) -> bool:
        """
        Check if the character is connected to this pipe.
        :param direction: The direction the character is in relation to this pipe.
        :param pipe: The character to check.
        :return: True if the character is connected to this pipe.
        """
        # Check if the direction is possible to be connected to self
        if direction not in self.connections[self.character] or pipe.character == ".":
            return False

        flip_directions = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }

        new_direction = flip_directions[direction]

        return new_direction in self.connections[pipe.character]
