#!usr/bin/env python3
"""Python version of Vectorize.R. Calculate the sum of a random matrix with size 100000"""
__appname__ = ""
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import sys
import numpy as np
import time
#import random

###global variables
np.random.seed(1)# set random seed
m = np.random.uniform(size = (1000, 1000)) #draw samples form a uniform distribution over the interval [0, 1).


###functions
def sum_all_elements_l(m):#sum all elements in matrix m using loop
    """using loop to sum all elements in m.
    flat attribute is an iterator over all elements of an array"""
    total = 0
    for element in m.flat: 
        total = total + element
    return total


def main(argv):
    """mian entry of the program"""
    start_l = time.time()# using time.time to record the executing time of a section of code
    sum_all_elements_l(m)
    end_l = time.time()
    print("USing python loop, the time taken is:")
    print(end_l - start_l)

    start_v = time.time()
    np.sum(m)
    end_v = time.time()
    print("Using the in-built numpy sum function, the time taken is:")
    print(end_v - start_v)
    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


