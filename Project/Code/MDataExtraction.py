#!usr/bin/env python3
"""read metadata from csv file"""
__appname__ = "Meta data extraction"
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
d = pd.read_csv("../Data/Merged_Data.csv")

def ExtractVal(x, t):
    """Extract value of label t from string x
       Return empty if no tabel"""
    pattern = r".*" + t + r":\s([^,]*).*"
    try:
        temp = re.search(pattern, x)
        return temp.group(1) if temp is not None else "NA"
    except:
        return "NA"

def main(argv):
    """main entry of the program"""
    global d, tags, tagsUni 
    #d.head()
    #d.columns
    #d.dtypes
    #d.shape (418745, 3)
    #remove redundant reletive paths to the source files
    d.SourceFile = d.SourceFile.str.extract(r'(\d+_.*)')
    d.insert(0, "Folder", d.SourceFile.str.extract(r'(\d+_.*)IMG'))
    d.insert(1, "ID", d.SourceFile.str.extract(r"(\d+)_"))
    d.insert(1, "ImageID", d.SourceFile.str.extract(r"IMG_(\d*)"))
    d.insert(1, "h", d.CreateDate.str.extract(r"\s(\d{2}):"))
    #for consistency
    d.Sequence = d.Sequence.str.extract(r"(\d*) of")
    d.Keywords = d.Keywords.str.replace(r"Human Presence", r"Human Presence: 1")
    d.Keywords = d.Keywords.str.replace(r"contact1", r"contact: 1")
    d.Keywords = d.Keywords.str.replace(r"contact2", r"contact: 2")
    d.Keywords = d.Keywords.str.replace(r"contact3", r"contact: 3")
    tags = d.Keywords.str.split(r",\s*")# split keywords by comma
    tagsUni = tags.explode()# flat the Series in order to use str.replace
    tagsUni = tagsUni.str.replace(r":.*", r"").unique()[0:10]# an array of unique label names
    tagsUni = tagsUni[~pd.isnull(tagsUni)]# remove nan
    for t in tagsUni:#apend new columns to the dataframe
        d[t] = d.Keywords.apply(ExtractVal, args = (t,))
    #d = d.replace("", np.nan, regex=False)# replace empty string with nan
    d.to_csv("../Data/New_Merged_Data.csv", index = False)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)