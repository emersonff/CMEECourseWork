#!usr/bin/env python3
"""get skeleton data in the first image of every sequence"""
__appname__ = "get first image of every sequence"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import os
import shutil
from datetime import datetime
#import glob

### globals
f = 'd_C2/'

def main(argv):
    global f
    d = []
    """main entry of the program"""
    for i, filename in enumerate(os.listdir(f)):
        with open(f + filename, 'rb') as imageFile:
            flag = 0
            if not imageFile.read().startswith(b'\xff\xd8'):
                print(f"{i}: {filename} - found!")
                flag = 1

            imageFile.seek(-2, 2)
            if imageFile.read() != b'\xff\xd9':
                print(f"{i}: {filename} - found!")
                flag = 1

            if flag == 1:
                d.append(filename)

    df = pd.DataFrame(d,columns=['SourceFile'])
    df.to_csv("../Corrupt_d_C2.csv", index = False)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)