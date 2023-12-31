import logging
from pprint import pprint

from Day3.Part1.part1 import Part1
from read_file import read_file_lines


def main():
    # part 1
    input_file = read_file_lines("input.txt")
    p1 = Part1(input_file)
    pprint(p1.symbols[0:10])
    pprint(p1.numbers[0:10])
    print(p1.puzzle_1())
    # part 2
    # input_file = read_input_file("test_input.txt")
    print(Part1(input_file).puzzle_2())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.disable(logging.DEBUG)
    main()
