#!usr/bin/env python3
"""Construct feature vectors from complete skeleton data and cluster them using PCA and k-means."""
__appname__ = "Clustering"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import json
import os
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import shutil
import Json
from matplotlib import pyplot as plt
import seaborn as sn
import Kp
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

### globals
d = pd.read_csv("../Results/Final_Data.csv")
#remve empty images
d = d[(d["SourceFile"] != "11_HH_26_4_18/DCIM/100_BTCF/IMG_1109.JPG")\
  & (d["SourceFile"] != "72_HH_1_6_18/100_BTCF/IMG_0009.JPG")]
samplelist = d["SourceFile"]
#len(samplelist)
dq = pd.read_csv("../Results/Seq_first_ske.csv")



def main(argv):
    """main entry of the program"""
    global d, samplelist, dq
    temp = Json.Json("../Data/p1/", 0.5 , 1)#read json files
    temp.CountCsv()
    dic = {k:v for (k, v) in temp.skeleton.items()}
    #len(temp.skeleton)
    #len(temp.fullske)
    l1 = list(dq["SourceFile"])
    temp_d = pd.DataFrame(columns=["V1","V2", "V3", "V4", "V5", "V6","V7", "V8", "V9", "V10","SourceFile"])
    for (k, v) in temp.skeleton.items():
        if k in l1:#filename
            for p in v:#for each skeleton
                try:
                    fv = Kp.Kp(p).fv#get feature vector
                    new_row = {"V1":fv[0], "V2":fv[1],"V3":fv[2],\
                               "V4":fv[3],"V5":fv[4], "V6":fv[5],\
                               "V7":fv[6], "V8":fv[7],"V9":fv[8], "V10":fv[9], "SourceFile" : k}
                    temp_d = temp_d.append(new_row, ignore_index=True)
                except:
                    print(k)
    features = ["V1","V2", "V3", "V4", "V5", "V6","V7", "V8", "V9", "V10"]
    x = temp_d.loc[:, features].values## Separating out the features
    y = temp_d.loc[:,['SourceFile']].values## Separating out the target
    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['1st principal component', '2nd principal component'])
    #finalDf= pd.concat([principalDf, dq[['SourceFile']]], axis = 1)

    for n_clusters in [2,3,4,5,6,7]:#calculate silhouette score for different number of clusters
        clusterer = KMeans(n_clusters=n_clusters)
        preds = clusterer.fit_predict(principalDf)
        #centers = clusterer.cluster_centers_
        score = silhouette_score(principalDf, preds)
        print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))

####k-means 3 clusters
    km = KMeans(init='k-means++', n_clusters=3)
    km_clustering = km.fit(principalDf)
    plt.scatter(principalDf["1st principal component"], principalDf["2nd principal component"],s =15, c=km_clustering.labels_, cmap='rainbow', alpha=0.7, edgecolors='b')
    #plt.title("5 poses")
    plt.xlabel("1st principal component")
    plt.ylabel("2nd principal component")
    #plt.show()
    plt.savefig('../Results/3pose_c.png')
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)