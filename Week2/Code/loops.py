#!/usr/bin/env python3

#For loops in python 
for i in range(5):
    print(i)

my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)

total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
    total = total + s#count the sum
    print(total)

# While loops in python

z = 0
while z < 100:
    z = z + 1
    print(z)

b = True
while b:
    print("Geronimo! infinite loop!  ctrl + c to stop!")
    #ctrl+c to stop!