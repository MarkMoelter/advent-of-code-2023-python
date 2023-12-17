class Pipe:
    def __init__(self, character: str, connections: dict[str, str]) -> None:
        self.character = character
        self.connections = connections

    def is_connected(self, direction: str, character: str) -> bool:
        """
        Check if the character is connected to this pipe.
        :param direction: The direction the character is in relation to this pipe.
        :param character: The character to check.
        :return: True if the character is connected to this pipe.
        """
        if direction not in self.connections:
            return False

        return character in self.connections[direction]
