import logging

from Day8.part_1 import Part1
from Day8.part_2 import Part2
from read_file import read_file_lines


def main():
    input_file = read_file_lines()
    # input_file = read_file_lines("test_input.txt")

    # part 1
    p1 = Part1(input_file)
    print(p1.solution())

    # part 2
    p2 = Part2(input_file)
    # print(p2.solution())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # logging.disable(logging.DEBUG)
    main()
