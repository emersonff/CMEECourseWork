#!usr/bin/env python3
"""Json class to read json files"""
__appname__ = "Json class "
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import os
import json
import Kp


class Json:
    """class Json"""


    def __init__(self, path, pr, nr):#constructor
        """constructor"""
        self.path = path# path to json files
        self.jsonFiles = [pos_json for pos_json in os.listdir(path)\
             if pos_json.endswith('.json')]#names of json files
        self.skeleton = self.getSkeleton(pr,nr)
        self.fullske = self.getFullSkeleton(pr, nr)

    def getSkeleton(self, pr, nr):
        """extract complete skeleton data from json files"""
        dic = {}
        for j in self.jsonFiles:
            with open(self.path + j) as f:
                data = json.load(f)
                name = j.replace("+", "/").replace("_keypoints.json", ".JPG")
                dic[name] = []
                for p in data["people"]:
                    temp = p["pose_keypoints_2d"][0:15 * 3]
                    if len([i for i in temp[2::3] if i >= pr]) >= nr:# first 15 keypoints
                        dic[name].append(temp)
        return {k: v for (k, v) in dic.items() if v}


    def getFullSkeleton(self, pr, nr):
        """extract complete skeleton data from json files"""
        dic = {}
        for j in self.jsonFiles:
            with open(self.path + j) as f:
                data = json.load(f)
                name = j.replace("+", "/").replace("_keypoints.json", ".JPG")
                dic[name] = []
                for p in data["people"]:
                    temp = p["pose_keypoints_2d"][0:15 * 3]
                    if (len([i for i in temp[2::3] if i >= pr]) >= nr) and (0 not in temp):# first 15 keypoints
                        dic[name].append(temp)
        return {k: v for (k, v) in dic.items() if v}


    def CountCsv(self):
        """return a csv file that contains the number of skeletons, file name and create date for
        images that contains at least one complete skeleton data."""
        d = pd.read_csv("../Data/Final_Data.csv")
        dic = {k:len(v) for (k, v) in self.fullske.items()}
        date = d.loc[d.SourceFile.isin(dic.keys()), ["SourceFile", "CreateDate", "h", "placeID"]]
        df = pd.DataFrame(list(dic.items()),columns = ["SourceFile","Count"])
        df = pd.merge(df, date, on = "SourceFile")
        df.to_csv("../Data/SkeletonCount.csv", index = False)
        return 0




    def getAllSke(self):
        """extract all skeleton data from json files no matter """
        dic = {}
        for j in self.jsonFiles:
            with open(self.path + j) as f:
                data = json.load(f)
                name = j.replace("+", "/").replace("_keypoints.json", ".JPG")
                dic[name] = 0
                for p in data["people"]:
                    temp = p["pose_keypoints_2d"]
                    if temp:# first 15 keypoints
                        dic[name] = 1
        return dic
    
    def getHuImage(self, pr, nr):
        """get skeleton data above a certain threshold. 
        p is the minimum probability to consider and nr is the minimum number of keypoints to consider. """
        dic = {}
        for j in self.jsonFiles:
            with open(self.path + j) as f:
                data = json.load(f)
                name = j.replace("+", "/").replace("_keypoints.json", ".JPG")
                dic[name] = 0
                for p in data["people"]:
                    temp = p["pose_keypoints_2d"][2::3]#taken account for all 25 keyponts
                    if len([i for i in temp if i >= pr]) >= nr:# the image will be considered as a human image
                        dic[name] = 1                         #if it has skeleton data that at least nr keypoints
        return dic                                            # has a probability greater than p
    
    
    



