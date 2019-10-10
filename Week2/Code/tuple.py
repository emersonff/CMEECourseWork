#!/usr/bin/env python3
"""python exercise tuple.py"""
# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehensions!
__appname__ = "tuple"
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

###function
def print_loop():
    """print every tuple on a separate line using a for loop"""
    #global birds
    for i in birds:
        a = str(i)
        print(a)
    return 0

def print_sep():
    """print every tuple on a separate line using * and sep operator"""
    #global birds
    print(*birds, sep = "\n") # *birds: unpacking the tuple "birds"
                              #sep = "\n" seperating each element in birds tuple using "\n"
    return 0


def main(argv):
    """main function"""
    print("loop:")
    print_loop()
    print("\n * and  sep operator: ")
    print_sep()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)