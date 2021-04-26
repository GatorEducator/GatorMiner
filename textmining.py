"""CLI Entry point"""
import json
import sys
import os

import src.analyzer as az
import src.summarizer as sz
import src.arguments as arg


if __name__ == "__main__":

    # Making a new directory to store the files.
    directory = "records"
    path = os.path.join(directory)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

    tm_arguments = arg.parse(sys.argv[1:])
    directory = tm_arguments.directory
    function = tm_arguments.function
    record = tm_arguments.record
    if function == "summary":
        # Determine if user wants to keep a record of the result.
        if record:
            # Write the summary into a json file.
            data = sz.summarizer(directory)
            file = open(path + "/" + record + ".json", "w")
            json.dump(data, file, indent=4)
            file.close()
        else:
            print(sz.summarizer(directory))
    elif function == "frequency":
        if record:
            data = az.dir_frequency(directory)
            file = open(path + "/" + record + ".json", "w")
            json.dump(data, file, indent=4)
            file.close()
        else:
            print(az.dir_frequency(directory))
