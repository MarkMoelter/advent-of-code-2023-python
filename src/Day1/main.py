from Part1.part1 import Part1
from Part2.part2 import Part2
from read_file import read_input_file


def main():
    # part 1
    input_file = read_input_file("input.txt")
    print(Part1(input_file).get_total())

    # part 2
    print(Part2(input_file).get_total())


if __name__ == '__main__':
    main()
