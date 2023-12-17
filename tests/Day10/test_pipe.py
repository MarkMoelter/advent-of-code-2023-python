import unittest

from src.Day10.part_1 import Pipe


class TestPipe(unittest.TestCase):
    def setUp(self):
        self.f_pipe = Pipe("F", {"S": "|LJ", "E": "-7"})

    def test_is_connected_returns_bool(self):
        result = self.f_pipe.is_connected("S", "|")

        self.assertIsInstance(result, bool)

    def test_is_connected_F_obj_input_S_oriented_pipe_char_returns_True(self):
        result = self.f_pipe.is_connected("S", "|")

        self.assertTrue(result)

    def test_is_connected_F_obj_input_S_oriented_period_char_returns_False(self):
        result = self.f_pipe.is_connected("S", ".")

        self.assertFalse(result)
