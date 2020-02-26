#!usr/bin/env python3
"""Population growth logistic equation model fitting"""
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
import seaborn as sns # You might need to install this (e.g., sudo pip install seaborn)

### globals
data = pd.read_csv("../Data/LogisticGrowthData.csv")

def main(argv):
    """main entry of the program"""
    global data
    data.dropna()# remove NAs
    data = data[(data.Time >= 0) & (data.PopBio > 0)]
    print("Loaded {} columns.".format(len(data.columns.values)))
    data.insert(0, "ID", data.Species + \
                "_" + data.Temp.map(str) \
                + "_" + data.Medium + "_" + data.Citation + "_" + data.Rep.map(str))

    #remove duplicated data
    data = data.drop_duplicates(subset = ["ID", "Time", "PopBio"])
    data = data.sort_values(["ID", "Time"], ascending = (True, True))
    data["lnN"] = np.log(data["PopBio"])
    data["log10N"] = np.log10(data["PopBio"])
    data.to_csv("../Data/NewData.csv")
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)