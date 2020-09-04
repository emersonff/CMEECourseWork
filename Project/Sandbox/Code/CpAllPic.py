#!usr/bin/env python3
""" Copy all pictures in to a single folder. """
__appname__ = "Copy Calibration data"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import shutil
#import glob

### globals
d = pd.read_csv("../Data/Final_Data.csv")

def main(argv):
    """main entry of the program"""
    global d
    #remove empty files
    d = d[(d["SourceFile"] != "11_HH_26_4_18/DCIM/100_BTCF/IMG_1109.JPG")\
         & (d["SourceFile"] != "72_HH_1_6_18/100_BTCF/IMG_0009.JPG")]
    samplelist = d["SourceFile"]
    for i in samplelist[200000:]:#seperate the job into two parts. Change here accordingly.
        src = i # initial path       
        dst = "A2/" + i.replace("/", "+")      # destination path
        try:   
            shutil.copyfile(src, dst)
        except:
            print(i + " cannot be copied") 
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)