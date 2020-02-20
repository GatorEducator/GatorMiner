"""Entry point"""
import sys

from src.util import analyzer as az
from src.util import summarizer as sz
from src.util import arguments

if __name__ == "__main__":
    tm_arguments = arguments.parse(sys.argv[1:])
    directory = tm_arguments.directory
    function = tm_arguments.function
    if function == "frequency":
        print(az.dir_frequency(directory))
    elif function == "summarize":
        print(sz.summarizer(directory))
