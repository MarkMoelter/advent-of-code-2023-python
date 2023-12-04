from dataclasses import dataclass


@dataclass
class Number:
    value: int
    x_span: tuple[int, int]
    y_pos: int
