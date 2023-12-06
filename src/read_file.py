def read_file_lines(filename: str = 'input.txt') -> list[str]:
    """
    Read the lines of the input file and remove newlines.
    :return: A list containing the lines of the file as the elements.
    """
    with open(filename, 'r') as f:
        return [ele.strip('\n') for ele in f.readlines()]


def read_file(filename: str = 'input.txt') -> str:
    """
    Read the input file.
    :param filename: The name of the file.
    :return: The file as a string.
    """

    with open(filename, 'r') as f:
        return f.read()
