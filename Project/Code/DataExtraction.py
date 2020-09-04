#!usr/bin/env python3
"""read metadata from csv file. Merge calibrated data."""
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
import glob
#import glob

### globals
d = pd.read_csv("../Data/data.csv")# data extracted uisng exiftool
d.SourceFile = d.SourceFile.str.extract(r'(\d+_.*)') # remove relative local paths


def ReplaceComma(x):
    """replace semicolon(s) between tags by comma(s)"""
    t = x.str.replace(r";",r",")
    t = t.str.replace(r",([^ ])",r";\1", n = 16)
    return t.str.replace(r",",r", ")

allFiles = glob.glob("../Data/data_from_camera/*.txt")# all calibrated data filenames
cali = [pd.read_table(item) for item in allFiles]
temp = pd.concat(cali, axis = 0)# read in one dataframe
a = temp.apply(ReplaceComma, axis = 1)# unify format
a.to_csv("../Results/Cali.txt", index = False)
cali_d = pd.read_table("../Results/Cali.txt", quotechar='\0',sep = ";")## convert calibrated data into dataframe

#camera information
camera = pd.read_csv("../Data/Camera.csv")
camera.SourceFile = camera.SourceFile.str.extract(r'(\d+_.*)')


def ExtractVal(x, t):
    """Extract value of label t from string x
       Return empty if no tabel"""
    pattern = r".*" + t + r":\s([^,]*).*"
    try:
        temp = re.search(pattern, x)
        return temp.group(1) if temp is not None else "NA"
    except:
        return "NA"


def MergeCali(df, d, camera):
    """Replace part of original data with calibrated dataset.
    df: calibrated dataset.  d: original dataset extracted using exiftool.
    camera: camera information. result: merged dataset"""
    df["Photo"] = df["Photo"].str.replace(r"\"", r"")#remove quoting marks
    df["Tags"] = df["Tags"].str.replace(r"\"", r"")#remove quoting marks
    df["Path"] = df["Path"].str.replace(r"\"", r"")#remove quoting marks
    #unify formats
    df["Date and Time"] = df["Date and Time"].str.replace(r"/", r":")
    df["Date and Time"] = df["Date and Time"].str.replace(r"(\d{2}):(\d{2}):(\d{4})", r"\3:\2:\1")
    df["SourceFile"] =df["Path"].str.extract(r'(\d+_HH.*)')# remove local path
    df["SourceFile"] =df["SourceFile"].str.replace(r"\\","/" )#unify format
    df = df[['SourceFile','Date and Time', 'Tags']]#remove redundant columns
    df.columns = ["SourceFile", "CreateDate", "Keywords"]#unify column names
    df.to_csv("../Results/Cali_Simp.csv", index = False)# save simplified calibrated data into csv for future use
    result = df.set_index('SourceFile').combine_first(d.set_index('SourceFile'))
    result = result.reset_index()#
    result = result.loc[result.SourceFile.isin(d.SourceFile)]# only save existed image data
    df2 = pd.merge(result, camera, on = "SourceFile")# add camera info
    return df2

def main(argv):
    """main entry of the program"""
    global cali_d, d, camera
    re = MergeCali(cali_d, d, camera) # merge calibarated data and camera info to orginal dataset
    
    re.SourceFile = re.SourceFile.str.extract(r'(\d+_.*)')
    re.insert(0, "Folder", re.SourceFile.str.extract(r'(\d+_.*)IMG'))
    re.insert(1, "ID", re.SourceFile.str.extract(r"(\d+)_"))
    re.insert(1, "ImageID", re.SourceFile.str.extract(r"IMG_(\d*)"))
    re.insert(1, "h", re.CreateDate.str.extract(r"\s(\d{2}):"))
    #for consistency
    re.Sequence = re.Sequence.str.extract(r"(\d*) of")
    re.Keywords = re.Keywords.str.replace(r"Human Presence", r"Human Presence: 1")
    re.Keywords = re.Keywords.str.replace(r"contact1", r"contact: 1")
    re.Keywords = re.Keywords.str.replace(r"contact2", r"contact: 2")
    re.Keywords = re.Keywords.str.replace(r"contact3", r"contact: 3")
    tags = re.Keywords.str.split(r",\s*")# split keywords by comma
    tagsUni = tags.explode()# flat the Series in order to use str.replace
    tagsUni = tagsUni.str.replace(r":.*", r"").unique()[0:10]# an array of unique label names
    tagsUni = tagsUni[~pd.isnull(tagsUni)]# remove nan
    for t in tagsUni:#apend new columns to the dataframe
        re[t] = re.Keywords.apply(ExtractVal, args = (t,))
    #re = re.replace("", np.nan, regex=False)# replace empty string with nan
    re.to_csv("../Results/New_Merged_Data.csv", index = False)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)