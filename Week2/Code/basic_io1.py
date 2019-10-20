"""###########################File Input"""

#open a file for reading
f = open("../Sandbox/test.txt", "r")
"""#use "implicit" for loop:
#if the object is a file, python will cycle over lines"""
for line in f:
    print(line)

#close the file
f.close()

#skip blank lines
f = open("../Sandbox/test.txt", "r")
for line in f:
    if len(line.strip()) > 0:
        print(line)

f.close()

