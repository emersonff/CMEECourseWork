#!usr/bin/env python3
"""Count how many feasible skeleton data in a specified folder.
Run it when ssh disconnect when running openpose"""
__appname__ = "Count skeleton data "
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as pl
import re
import os
import json
import shutil
#import glob

### globals
#d = pd.read_csv("../Data/Merged_Data.csv")
path_to_json = "../p1/"
path_to_pic = "C1/"
dst = "C1_1/"
def main(argv):
    """main entry of the program"""
    #read names of json files, should be the same for all three models
    #path_to_json = "../p2/"
    global path_to_json, path_to_pic, dst
    if not os.path.exists(dst):
	    os.mkdir(dst)
    jsonFiles = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    result = [path_to_pic + j.replace("_keypoints.json", ".JPG") for j in jsonFiles]
    for i in result:
        try:   
            shutil.move(i, dst)
        except:
            print(i + " cannot be moved") 
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)