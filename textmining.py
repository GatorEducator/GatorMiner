"""CLI Entry point"""
import json
import sys

import src.analyzer as az
import src.summarizer as sz
import src.arguments as arg

#def save_data(data, directory):
    # do stuff here

if __name__ == "__main__":
    tm_arguments = arg.parse(sys.argv[1:])
    directory = tm_arguments.directory
    function = tm_arguments.function
    record = tm_arguments.record
    if function == "frequency":
        if record:
            #save documents
            #print("saving")
            data = sz.summarizer(directory)
            file = open(record + ".json", "w")
            json.dump(data, file, indent=4)
            file.close()
        else:
            print("printing")
    elif function == "summary":
        print("here")
        #print(sz.summarizer(directory))
