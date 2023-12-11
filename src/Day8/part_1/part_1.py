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

    def solution(self, start_node: str, end_node: str) -> int:
        """
        Count the number of iterations needed for the turing machine to stop (reaches ZZZ).
        :param start_node: The node to start at.
        :param end_node: The node to end at.
        :return: The number of iterations before it stops.
        """
        count = 0
        current_node = start_node
        while current_node != end_node:
            for l_or_r in self.instructions:
                count += 1

                # Set the current node
                left, right = self._network[current_node]

                if l_or_r == "L":
                    current_node = left
                else:
                    current_node = right

                # Break out of for loop prematurely if end node is found
                if current_node == end_node:
                    break

        return count
