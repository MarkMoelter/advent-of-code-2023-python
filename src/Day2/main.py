from Day2.Part1.part1 import Part1
from read_file import read_input_file


def main():
    input_file = read_input_file()
    # part 1
    print(Part1((12, 13, 14), input_file).add_game_ids_of_possible_games())
    # part 2


if __name__ == '__main__':
    main()
