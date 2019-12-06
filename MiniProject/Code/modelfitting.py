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
import scipy.integrate as integrate

### global variables
df = pd.read_csv("../Data/LogisticGrowthData.csv", sep = ",")
grouped = df.groupby(["Species", "Temp", "Medium"])#285
for name, group in grouped:
    print(name)
    print(group)

### global functions

def main(argv):
    """main entry point of the program"""
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


