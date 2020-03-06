#!usr/bin/env python3
"""Bacterial growth model fittings. 
This script is used for handling data"""
__appname__ = "Model fitting"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import pandas as pd 
import scipy as sc
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as pl

### globals
data = pd.read_csv("../Data/LogisticGrowthData.csv")#import original dataset

def main(argv):
    """main entry of the program"""
    global data
    data.dropna()# remove NAs
    #only keep row that is reasonable
    data = data[(data.Time >= 0) & (data.PopBio > 0)]
    #insert a new column called ID which is used for identify sub datasets
    data.insert(0, "ID", data.Species + \
                "_" + data.Temp.map(str) \
                + "_" + data.Medium + "_" + data.Citation + "_" + data.Rep.map(str))

    #remove duplicated data
    data = data.drop_duplicates(subset = ["ID", "Time", "PopBio"])
    #sort the whole data set by ascending order of ID and time
    data = data.sort_values(["ID", "Time"], ascending = (True, True))
    #used natural logarithm of PopBio
    data["lnN"] = np.log(data["PopBio"])
    #data["log10N"] = np.log10(data["PopBio"])
    data.to_csv("../Results/NewData.csv")
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)