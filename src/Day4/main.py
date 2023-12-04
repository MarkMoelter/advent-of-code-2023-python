import logging

from Day4.Part1.part1 import Part1
from read_file import read_input_file


def main():
    # part 1
    input_file = read_input_file("input.txt")
    p1 = Part1(input_file)
    print(p1.puzzle_1())
    # part 2


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.disable(logging.DEBUG)
    main()
