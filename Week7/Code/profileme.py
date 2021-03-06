#!usr/bin/env python3
"""profiling in python"""
__appname__ = "profileme.py"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

def my_squares(iters):
    """using for-loop to execute list.append()"""
    out = []
    for i in range(iters):
        out.append(i ** 2)
    return out

def my_join(iters, string):
    """using for-loop to execute string.join()."""
    out = ''
    for i in range(iters):
        out += string.join(", ")
    return out

def run_my_funcs(x,y):
    """run two functions above."""
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
#run -p profileme.py 