#!/usr/bin/env python3
"""Python practical cfexercise2.py"""
__appname__ = "cfexercise2"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.2"
__license__ = "none"

###imports###
import sys

###functions###
def foo_1(x = 12):
    """ print hello every time find a number in [0, x) that is a multiple of 3.""" 
    for j in range(x):
        if j % 3 == 0:
            print("hello")
    return 0

def foo_2(x = 15):
    """print hello every time find a number y in [0, x) that y mod 4 or 5 is equal to 3.""" 
    for j in range(x):
        if j % 5 == 3:
            print("hello")
        elif j % 4 == 3:
            print("hello")
    return 0

def foo_3(x = 15):
    """print numbers in [0, x) with a interval of 3"""
    z = 0
    while z != x:
        print("hello")
        z = z + 3
    return 0

def foo_4(x = 12, y = 100):
    """search in [x, y). if 31 is in that interval, print 'hello' 7 times. Otherwise if 18 is in the 
    interval, print 'hello' once. """
    z = x
    while z < y:
        if z == 31:
            for k in range(7):
                print("hello")
        elif z == 18:
            print("hello")
        z = z + 1
    return 0
    
def main(argv):
    """Main entry point of the program"""
    foo_1()
    foo_2()
    foo_3()
    foo_4()
    return 0

if __name__ == "__main__":
    """Makes sure the "main" function is called from command line"""
    status = main(sys.argv)
    sys.exit(status)


    