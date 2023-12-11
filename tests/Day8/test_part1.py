import unittest

from src.Day8.part_1 import Part1
from src.read_file import read_file_lines


class TestPart1(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Part1(
            read_file_lines(r"C:\Users\marke\PycharmProjects\advent-of-code-2023-python\src\Day8\test_input.txt"))

    def test_network_dict_contains_key_AAA_and_val_tuple_BBB_and_CCC(self):
        result = self.p1.network

        expected = {"AAA": ("BBB", "CCC")}

        self.assertDictEqual(result, expected | result)
