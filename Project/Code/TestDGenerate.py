#!usr/bin/env python3
"""Get test data from calibrated dataset"""
__appname__ = "Test dataset generatation"
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
#import glob

### globals
cali = pd.read_csv("../Results/Cali_Simp.csv")
d = pd.read_csv("../Results/Final_Data.csv")



def main(argv):
    """main entry of the program"""
    temp = d.loc[d.SourceFile.isin(cali.SourceFile),["SourceFile", "species1", "Human.Presence", "contact", "species2", "species3", "Sp"]]
    #temp["species1"].unique()
    #temp["species2"].unique()
    #temp["species3"].unique()
    #temp["Human.Presence"].unique()
    #temp["contact"].unique()
    #temp["Sp"].unique()
    #temp.count()
    #temp["species1"].value_counts()
    hu = temp.loc[(temp["species1"] == 'Human') | (temp["Human.Presence"] == 1)]
    hu.count()#9481

    notHu = temp.loc[(temp["species1"] != 'Human') & (temp["Human.Presence"] != 1)]
    notHu.count()
    notHu = notHu.head(9481)

    hu.to_csv("../Results/SampleHu.csv", index = False)#9481 human images
    notHu.to_csv("../Results/SampleNotHu.csv", index = False)#9481 non-human images
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)