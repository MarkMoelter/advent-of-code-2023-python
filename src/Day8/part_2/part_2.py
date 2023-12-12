import logging

from src.Day8.part_1 import Part1

logger = logging.getLogger(__name__)


class Part2(Part1):
    def __init__(self, input_file: list[str]) -> None:
        super().__init__(input_file)

    def naive_solution(self, start_node_suffix: str, end_node_suffix: str) -> int:
        """
        Count the number of iterations needed for the turing machine to stop (reaches ZZZ).
        :param start_node_suffix: The suffix that each start node has.
        :param end_node_suffix: The suffix that each end node has.
        :return: The number of iterations before it stops.
        """
        count = 0
        current_nodes = [node for node in self.network if node.endswith(start_node_suffix)]

        all_nodes_have_end_suffix = False

        i = 0
        # End loop when all nodes end with the end node suffix
        while not all_nodes_have_end_suffix:
            for l_or_r in self.instructions:
                new_nodes = []
                # Set the current node
                for node in current_nodes:
                    left, right = self.network[node]
                    if l_or_r == "L":
                        new_nodes.append(left)
                    else:
                        new_nodes.append(right)

                if "XXX" in new_nodes:
                    raise ValueError("Nodes became stuck")

                current_nodes = new_nodes

                nodes_with_end_suffix = [node.endswith(end_node_suffix, -1) for node in current_nodes]
                all_nodes_have_end_suffix = all(nodes_with_end_suffix)

                if any(nodes_with_end_suffix):
                    logger.debug(f"{count}")

                count += 1

                if all_nodes_have_end_suffix:
                    break

        return count
