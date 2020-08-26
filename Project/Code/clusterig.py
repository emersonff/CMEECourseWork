#!usr/bin/env python3
import sys
import json
import os
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import shutil
import Json
import Kp
d = pd.read_csv("../Data/Final_Data.csv")
#remve empty images
d = d[(d["SourceFile"] != "11_HH_26_4_18/DCIM/100_BTCF/IMG_1109.JPG")\
  & (d["SourceFile"] != "72_HH_1_6_18/100_BTCF/IMG_0009.JPG")]
samplelist = d["SourceFile"]
len(samplelist)

temp = Json.Json("../Data/p1/")

dq = pd.read_csv("../Data/Seq_first_ske.csv")
#dq["SourceFile"]

l1 = list(dq["SourceFile"])
temp_d = pd.DataFrame(columns=["V1","V2", "V3", "V4", "V5", "V6","V7", "V8", "V9", "V10","SourceFile"])
for (k, v) in temp.skeleton.items():
    if k in l1:#filename
        for p in v:#for each skeleton
            fv = Kp.Kp(p).fv#get feature vector
            new_row = {"V1":fv[0], "V2":fv[1],"V3":fv[2],\
                       "V4":fv[3],"V5":fv[4], "V6":fv[5],\
                       "V7":fv[6], "V8":fv[7],"V9":fv[8], "V10":fv[9], "SourceFile" : k}
            temp_d = temp_d.append(new_row, ignore_index=True)
