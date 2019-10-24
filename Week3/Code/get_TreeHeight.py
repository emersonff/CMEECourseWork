#!usr/bin/env python3
"""Python version of get_TreeHeight.R. calculate the tree heights from an input csv file and save the results in Results directory.  """
__appname__ = "Get TreeHeight"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import sys
import numpy as np 
import csv
import pandas as pd
import re #regular expressions
###globals


###functions
def TreeHeight(m):#m[0]: species;    m[1]: distance in meter    m[2]:degrees
    """calculates tree heights.
    input: m where m[:,0]: species;    m[:,1]: distance in meter    m[:,2]:degrees
    output: a list contians all heights """
    radians = m[:,2].astype("float") * np.pi /180 ##coerce from character to numeric type for calculation
    heights =m[:,1].astype("float") * np.tan(radians) 
    return heights


def main(argv):
    """main entry of the program"""
    trees = pd.read_csv(argv[1])#read file
    trees_m = trees.values#convert to array
    heights = TreeHeight(trees_m)#calculate heights
    trees["Tree.Height.m"] = heights
    filename = "../Results/" + re.split("\\.|/", argv[1])[4] + "_treeheights.csv"
    print ("writng to result file...")
    trees.to_csv(filename)
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)