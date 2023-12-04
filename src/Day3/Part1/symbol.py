from dataclasses import dataclass


@dataclass
class Symbol:
    """
    A class representing a symbol.

    Attributes:
        char (str): The value of the symbol.
        x_pos (int): The x position of the symbol.
        y_pos (int): The y position of the symbol.
    """
    char: str
    x_pos: int
    y_pos: int
