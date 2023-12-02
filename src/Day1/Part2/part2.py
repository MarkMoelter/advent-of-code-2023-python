from Day1.Part1.part1 import Part1


class Part2(Part1):
    def __init__(self, input_file: list[str]):
        super().__init__(input_file)

    @staticmethod
    def get_first_digit(input_line: str, last: bool = False) -> str:
        spelled_out = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        spelled_to_int = {num: str(idx) for idx, num in enumerate(spelled_out)}

        spelled_out.extend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        index_dict = {}

        # Get the index of each digit
        for val in spelled_out:
            if last:
                index = input_line.rfind(val)
            else:
                index = input_line.find(val)
            if index != -1:
                index_dict[index] = val

        if last:
            first_digit = index_dict[max(index_dict.keys())]
        else:
            first_digit = index_dict[min(index_dict.keys())]

        if first_digit.isdigit():
            return first_digit

        return spelled_to_int[first_digit]

    def get_double_digit(self, input_line: str) -> int:
        first_digit = self.get_first_digit(input_line)
        last_digit = self.get_first_digit(input_line, last=True)

        return int(first_digit + last_digit)
