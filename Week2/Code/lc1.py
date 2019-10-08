#!/usr/bin/env python3
"""lc1"""
#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 
__appname__ = ""
__author__ = "Xiang Li"
__version__ = "0.0.1"
__license__ = "none"

###imports
import sys

###global variables
birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )


###functions
def lc():
    """list comprehensions"""
    global birds
    latin_name = [i[0] for i in birds] #  list that stores latin names
    common_name = [i[1] for i in birds] #  list that stores common names
    mass = [i[2] for i in birds] # list stores body masses
    print(latin_name)
    print(common_name)
    print(mass)
    return 0

def loops():
    """conventional loops"""
    global birds
    latin_name = list()
    common_name = list()
    mass = list()
    for i in birds:
        latin_name.append(i[0])
        common_name.append(i[1])
        mass.append(i[2])
    print(latin_name)
    print(common_name)
    print(mass)  


    return 0

def main(argv):
    """main function"""
    lc()
    print("\n")
    loops()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


