"""Entry point"""
import sys

from src import analyzer as az
from src import summarizer as sz
from src import arguments

if __name__ == "__main__":
    tm_arguments = arguments.parse(sys.argv[1:])
    directory = tm_arguments.directory
    function = tm_arguments.function
    if function == "frequency":
        print(az.dir_frequency(directory))
    elif function == "summary":
        print(sz.summarizer(directory))
