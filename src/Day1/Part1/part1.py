class Part1:
    def __init__(self, input_file: list[str]):
        self.input_file = input_file

    @staticmethod
    def get_first_digit(input_line: str) -> str:
        """
        Get the first digit from the input line.
        :param input_line: The input line as a string.
        :return: The first digit in the input.
        """
        for char in input_line:
            if char.isdigit():
                return char

    def get_double_digit(self, input_line: str) -> int:
        """
        Get the double-digit number form the input line.
        :param input_line: The input line as a string.
        :return: The two digits
        """
        reversed_input = input_line[::-1]

        first_digit = self.get_first_digit(input_line)
        last_digit = self.get_first_digit(reversed_input)

        return int(first_digit + last_digit)

    def get_total(self) -> int:
        total = 0
        for line in self.input_file:
            total += self.get_double_digit(line)

        return total
