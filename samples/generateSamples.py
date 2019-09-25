import random

num = int(input("How many sample files do you want to create?: "))
fName = input("What should the name of the output file be?: ")


for i in range(num):
    file = open("./" + fName + str(i+1) + ".md", "w")
    file.write("Name: " + "Student " + str(i+1) + "\n")
    for j in range(random.randint(1,5)):
        file.write("\n[TAG]\n")
        for k in range(random.randint(5,30)):
            file.write("Some Text ")
    file.close()
    
