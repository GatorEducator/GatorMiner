"""Read file"""


def read_file(filepath):
    """Read the value from the filepath"""
    with open(filepath) as file:
        chosen_line = file.readline().replace("\n", "")
        return chosen_line
