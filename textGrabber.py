#!/usr/bin/env python3

# Written by: Danny Ullrich
# email: ullrichd@allegheny.edu
# Date: 9/18/2019
def help():
    print("\tWelcome to the survey text grabbing application!")
    print("\tTo run this program please use the following command:")
    print("\t\tpython3 textgrabber.py [surveyFileLocation]")
#end help()

def getFile(inputFile): #Gets the file, outputs survey contents into a list
    with open(inputFile) as file:
        multi = False
        data = file.readlines()
        sorted = []
        build = ""
        for line in data:
            #print(line)
            if multi:
                if "[" and "]" not in line:
                    build += " " + line.replace("\n"," ")
                    #print("NO TAG:",line)
                else:
                    #print("TAG FOUND, MULTI FALSE:",line)
                    sorted.append(build)
                    multi = False
                    build = ""
            if "Name:" in line and multi == False:
                sorted.append((line.replace("Name: ","").replace("\n","")))
                #sorted.update({"Name" : line.replace("Name: ","").replace("\n","")})

            if "[" and "]" in line:
                    multi = True
        sorted.append(build)
        #print(sorted)
        return sorted

def buildSample(dic, list, name): #builds a dictionary of text examples.
    dic.update({name : list})



def begin(task_str):
    sampleDic = {}
    if len(glob.glob(task_str)) > 1:
        for file in glob.glob(task_str):
            list = getFile(file)
            buildSample(sampleDic, list, list[0])
    else:
        list = getFile(task_str)
        buildSample(sampleDic, list, list[0])

    print("Would you like to output the entire dictionary? [y/n]")
    str = input()
    if str.lower() == "y":
        print(sampleDic)

    print("Would you like to see a specific student? [y/n]")
    str = input()

    if str.lower() == "y":
        str = input("Please enter a student name: ")
        if str in sampleDic:
            print(sampleDic.get(str))
        else:
            print("Student not found!")

    print("Would you like to output the data? [y/n]")
    str = input()

    if str.lower() == "y":
        name = input("Output file name?: ")
        file = open("output/" + name + ".txt", "w")
        for key in sampleDic:
            file.write("------- START SAMPLE -------\n")
            data = sampleDic[key]
            iterdata = iter(data)
            next(iterdata)
            for data in iterdata:
                print(data)
                file.write(data + "\n")
            file.write("------- END SAMPLE -------\n")
        file.close()




import os, sys, glob

if __name__ == '__main__':

        if len(sys.argv) == 2:
                begin(sys.argv[1])
        else:
                help()
                sys.exit()
