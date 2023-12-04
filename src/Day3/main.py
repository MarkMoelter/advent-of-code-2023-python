import logging
from pprint import pprint

from Day3.Part1.part1 import Part1
from read_file import read_input_file


def main():
    # part 1
    input_file = read_input_file("input.txt")
    pprint(Part1(input_file).symbols[0:10])
    # part 2


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
