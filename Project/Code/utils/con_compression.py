#!usr/bin/env python3
""" compressed remained images. run it if ssh disconnected when you are running image_compression """
__appname__ = "Continue compress images"
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
import os

### globals
#d = pd.read_csv("../Data/Final_Data.csv")
original_path = "A1/"
dest_path = "A1_1/"
c_path = "c_C1/"
def main(argv):
    """main entry of the program"""
    global original_path, dest_path,c_path
    original_file = os.listdir(original_path)#orginal files
    c_file = os.listdir(c_path)# already compressed files
    dest_file = list(set(original_file).difference(c_file)) # files aimed to copied into a new dest
    #samplelist = d["SourceFile"]
    for i in dest_file:#seperate the job into two parts. Change here accordingly.
        src = original_path + i # initial path       
        dst = dest_path + i      # destination path
        try:   
            shutil.copyfile(src, dst)
        except:
            print(i + " cannot be copied") 
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)