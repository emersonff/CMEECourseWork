#!usr/bin/env python3
"""get skeleton data in the first image of every sequence"""
__appname__ = "get first image of every sequence"
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
from datetime import datetime
#import glob

### globals
int_low = 0#time interval
int_up = 24
seq_interval = 30 #every 45 seconds
d = pd.read_csv("../Data/SkeletonCount.csv")

def main(argv):
    """main entry of the program"""
    global int_low, int_up, seq_interval, d
    image_list = [] # list of filenames of first images
    d.insert(0, "Folder", d.SourceFile.str.extract(r'(\d+_.*)IMG'))
    d.insert(1, "ImageId", d.SourceFile.str.extract(r'IMG_(\d*).JPG'))
    d = d.loc[(d["h"] >= int_low) & (d["h"] <= int_up)] # time interval

    for f in d["Folder"].unique():
        subd = d.loc[d["Folder"] == f].sort_values(by=['ImageId']).reset_index().drop(columns =["index"])
        i = 0
        while i < len(subd):
            current = subd.loc[i]["SourceFile"]
            image_list.append(current)
            t1 = datetime.strptime(subd.loc[i]["CreateDate"], '%Y:%m:%d %H:%M:%S')
            j = i + 1
            if j < len(subd):
                t2 = datetime.strptime(subd.loc[j]["CreateDate"], '%Y:%m:%d %H:%M:%S')
                diff = (t2 - t1).total_seconds()
                while (diff < seq_interval) & (j < len(subd) - 1):
                    j = j + 1
                    t2 = datetime.strptime(subd.loc[j]["CreateDate"], '%Y:%m:%d %H:%M:%S')
                    diff = (t2 - t1).total_seconds()   
            i = j
    df = d.loc[d.SourceFile.isin(image_list), ]
    df.to_csv("../Data/Seq_first_ske.csv", index = False)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)