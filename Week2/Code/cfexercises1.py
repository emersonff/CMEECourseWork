#!/usr/bin/env python3
###imports
import sys

#what does each of foo_x do?
def foo_1(x):
    """return x power 0.5"""
    return x ** 0.5

def foo_2(x, y):
    """accept 2 numbers and return the bigger one"""
    if x > y:
        return x
    return y

def foo_3(x, y, z):
    """ return [x, y ,z] if x <= y and y <= z
    if x > y and x <= z return [y, x, z]
    if x > y and x > z return [y, z, x] """
    if x > y:
        tmp = y
        y = x 
        x = tmp 
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo_4(x):
    """calculate the factorial of x"""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x):
    """ a recursive function that calculates the factorial of x"""
    if x == 1:
        return 1
    return x*foo_5(x-1)

def foo_6(x): 
    """calculate the factorial of x in a different way"""
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto


def main(argv):
    """Main entry point of the program"""
    foo_1(12)
    foo_2(23 ,33)
    foo_3(45,222,33)
    foo_4(15)
    foo_5(12)
    foo_6(213)
    return 0

if __name__ == "__main__":
    """Makes sure the "main" function is called from command line"""
    status = main(sys.argv)
    sys.exit(status)



