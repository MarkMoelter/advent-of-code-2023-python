def read_input_file(filename='input.txt') -> list[str]:
    """
    Read the lines of the input file and remove newlines.

    :return: A list containing the lines of the file as the elements.
    """
    with open(filename, 'r') as f:
        return [ele.strip('\n') for ele in f.readlines()]
