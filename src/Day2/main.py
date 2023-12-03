from Day2.Part1.part1 import Part1
from read_file import read_input_file


def main():
    input_file = read_input_file()
    # part 1
    print(Part1(input_file).add_game_ids_of_possible_games((12, 13, 14)))
    # part 2
    print(Part1(input_file).sum_of_powers_of_lowest_needed_cubes())


if __name__ == '__main__':
    main()
