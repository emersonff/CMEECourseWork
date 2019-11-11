#!usr/bin/env python3
"""loops vs. list comprehensions: which is faster?"""
__appname__ = ""
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import timeit
import time
from profileme import my_squares as my_squares_loops
from profileme import my_squares as my_squares_lc

iters =  1000000

# %timeit(my_join_join(iters, mystring))
# %timeit(my_join(iters, mystring))
start = time.time()
my_squares_loops(iters)
print("my_squares_loops takes %f s to run." % (time.time() - start))

start = time.time()
my_squares_lc(iters)
print("my_squares_lc takes %f s to run." % (time.time() - start))