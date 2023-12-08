import logging

from read_file import read_file_lines
from Day6.part_1 import Part1
from Day6.part_2 import Part2


def main():
    input_file = read_file_lines()
    # input_file = read_file_lines("test_input.txt")

    # part 1
    p1 = Part1(input_file)
    print(p1.solution())

    # Only need to check the first half of the time, each half is a mirror of each other.
    # Check number of times you will beat record, dfs where end is > than the current record. -> Recursion

    # part 2
    p2 = Part2(input_file)
    print(p2.solution())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # logging.disable(logging.DEBUG)
    main()
