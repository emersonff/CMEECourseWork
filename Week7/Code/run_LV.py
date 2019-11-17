#!usr/bin/env python3
"""Run both LV models and profile these scripts."""
__appname__ = "run_LV"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import os

# can`t using magic command within a script
# %timeit(my_join_join(iters, mystring))
# %timeit(my_join(iters, mystring))
os.system("python -m cProfile LV1.py")
os.system("python -m cProfile LV2.py 1 0.1 1.5 0.75 15000")
os.system("python -m cProfile LV3.py")
os.system("python -m cProfile LV4.py")