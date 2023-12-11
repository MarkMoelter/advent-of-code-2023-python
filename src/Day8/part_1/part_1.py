import logging
import re

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self.instructions = input_file[0]
        self._network = self.network

    @property
    def network(self) -> dict[str, tuple[str, str]]:
        """
        Map the network from the input file as a dictionary.
        :return: The network as a dict with each nodes value mapped to its left and right states.
        """
        out = {}
        for line in self.input_file[2:]:
            node_left_right = tuple(re.findall(r"\w+", line))

            if len(node_left_right) != 3:
                raise ValueError("Invalid node")
            out[node_left_right[0]] = node_left_right[1], node_left_right[2]

        return out
