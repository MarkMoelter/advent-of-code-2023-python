import unittest

from src.Day10.part_1 import Pipe, Direction


class TestPipe(unittest.TestCase):
    def setUp(self):
        self.ground = Pipe(".", (0, 0))
        self.start_pipe = Pipe("S", (0, 0))
        self.f_pipe = Pipe("F", (0, 0))
        self.l_pipe = Pipe("L", (0, 0))
        self.j_pipe = Pipe("J", (0, 0))
        self.hori_pipe = Pipe("-", (0, 0))
        self.vert_pipe = Pipe("|", (0, 0))

    def test_is_connected_returns_bool(self):
        result = self.f_pipe.is_connected(Direction.SOUTH, self.vert_pipe)

        self.assertIsInstance(result, bool)

    def test_is_connected_F_obj_input_south_oriented_pipe_char_returns_true(self):
        result = self.f_pipe.is_connected(Direction.SOUTH, self.vert_pipe)

        self.assertTrue(result)

    def test_is_connected_F_obj_input_south_oriented_period_char_returns_false(self):
        result = self.f_pipe.is_connected(Direction.SOUTH, self.ground)

        self.assertFalse(result)

    def test_is_connected_F_obj_input_east_oriented_j_char_returns_true(self):
        result = self.f_pipe.is_connected(Direction.EAST, self.j_pipe)

        self.assertTrue(result)

    def test_is_connected_F_obj_input_east_oriented_L_char_returns_false(self):
        result = self.f_pipe.is_connected(Direction.EAST, self.l_pipe)

        self.assertFalse(result)

    def test_is_connected_start_pipe_input_east_oriented_L_char_returns_false(self):
        result = self.start_pipe.is_connected(Direction.EAST, self.l_pipe)

        self.assertFalse(result)

    def test_is_connected_start_pipe_input_west_oriented_L_char_returns_false(self):
        result = self.start_pipe.is_connected(Direction.WEST, self.l_pipe)

        self.assertTrue(result)

    def test_is_connected_L_pipe_input_east_oriented_start_pipe_returns_true(self):
        result = self.l_pipe.is_connected(Direction.EAST, self.start_pipe)

        self.assertTrue(result)
