import logging

from read_file import read_input_file
from .part_1.part_1 import Part1
from .part_2.part_2 import Part2


def main():
    input_file = read_input_file()
    input_file = read_input_file("test_input.txt")

    # part 1
    p1 = Part1(input_file)

    # part 2
    p2 = Part2(input_file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # logging.disable(logging.DEBUG)
    main()
