#!usr/bin/env python3
""" Copy all pictures recorded in calibration data set to the specified folder
This script should be placed under the mian folder of all pictures."""
__appname__ = "Copy Calibration data"
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
import shutil
#import glob

### globals
cali = pd.read_csv("../Results/Cali_Simp.csv")#Path to csv file. Change here accordingly
d = pd.read_csv("../Results/Final_Data.csv")

def main(argv):
    """main entry of the program"""
    global cali, d
    temp = d.loc[d.SourceFile.isin(cali.SourceFile),["SourceFile","species1", "Human.Presence", "contact", "species2", "species3", "Sp"]]
    temp.count()
    temp["species1"].value_counts()
    hu = temp.loc[(temp["species1"] == 'Human') | (temp["Human.Presence"] == 1)]
    hu.count()
    notHu = temp.loc[(temp["species1"] != 'Human') & (temp["Human.Presence"] != 1)]
    notHu.count()
    notHu = notHu.head(9481)

    samplelist = notHu["SourceFile"]
    for i in samplelist:
        src = i # initial path
        
        dst = "Sample/" + i.replace("/", "+")      # destination path
        shutil.copy(src, dst)

    samplelist = hu["SourceFile"]
    for i in samplelist:
        src = i # initial path
        
        dst = "Sample/" + i.replace("/", "+")      # destination path
        shutil.copy(src, dst)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)