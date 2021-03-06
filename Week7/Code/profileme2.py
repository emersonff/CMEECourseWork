#!usr/bin/env python3
"""profiling in python
using list comprehension instead of loop;
replaced the .join with an explicit string concatenation."""
__appname__ = "profileme2.py"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import scipy as sc

def my_squares(iters):
    """list comprehension"""
    out = [i ** 2 for i in range(iters)]
    return out

def my_squares_matrix(iters):
    """preallocate anarray instead of using a list"""
    out = sc.array([ i ** 2 for i in range(iters)])
    return out


def my_join(iters, string):
    """join string with comma for iters number of iteration."""
    out = ''
    for i in range(iters):
        out += ", " + string
    return out

def run_my_funcs(x,y):
    """run two functions above."""
    print(x,y)
    my_squares(x)
   # my_squares_matrix(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
#run -p profileme2.py