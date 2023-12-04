from dataclasses import dataclass


class Symbol(dataclass):
    character: str
    x_pos: int
    y_pos: int
