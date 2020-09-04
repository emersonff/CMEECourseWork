#!usr/bin/env python3
"""Compare the performance of human classification between the Openpose library(BODY-25)
and cnn + mlp human classifier"""
__appname__ = "Classifier comparison"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
#import json
import os
import pandas as pd #'1.0.4'
import scipy as sc
import numpy as np
import re
import shutil
#import Json
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
import Json

### globals
#read classifer results
c1 = pd.read_csv("../Data/human_MLP_predictions_C1.csv")
c2 = pd.read_csv("../Data/human_MLP_predictions_C2.csv")
d = pd.read_csv("../Results/SkeletonCount.csv")
cor_d1 = pd.read_csv("../Data/Corrupt_d_C1.csv")
cor_d2 = pd.read_csv("../Data/Corrupt_d_C2.csv")
df = pd.read_csv("../Results/Final_Data.csv")

#concat the results into one
cor_d = pd.concat([cor_d1, cor_d2])
c = pd.concat([c1, c2])

#unify formats
c.SourceFile = c.SourceFile.str.extract(r"(?:c_C1+/|c_C2+/)(.*)")
c.SourceFile = c.SourceFile.str.replace("+", "/")
cor_d.SourceFile = cor_d.SourceFile.str.replace("+", "/")
df = df[df.SourceFile.isin(c.SourceFile)]#remove corrupt data from orginal dataset
d = d.drop(d[d.SourceFile.isin(cor_d.SourceFile)].index)#remove corrupt data

#test dataset
hu = pd.read_csv("../Results/SampleHu.csv")
notHu = pd.read_csv("../Results/SampleNotHu.csv")
actual1 = pd.DataFrame(np.ones(9481),index = hu.SourceFile, columns = ["actual"])
actual2 = pd.DataFrame(np.zeros(9481),index = notHu.SourceFile, columns = ["actual"])
test_d = pd.concat([actual1, actual2])
#test_d

def convert1(x):
    if x == "human":
        return 1
    else:
        return 0

def cm_analysis(y_true, y_pred, filename, labels, ymap=None, figsize=(10,10), Actual = "Actual", Predicted = "Predicted"):
    """
    Generate matrix plot of confusion matrix with pretty annotations.
    The plot image is saved to disk.
    args: 
      y_true:    true label of the data, with shape (nsamples,)
      y_pred:    prediction of the data, with shape (nsamples,)
      filename:  filename of figure file to save
      labels:    string array, name the order of class labels in the confusion matrix.
                 use `clf.classes_` if using scikit-learn models.
                 with shape (nclass,).
      ymap:      dict: any -> string, length == nclass.
                 if not None, map the labels & ys to more understandable strings.
                 Caution: original y_true, y_pred and labels must align.
      figsize:   the size of the figure plotted.
    """
    if ymap is not None:
        y_pred = [ymap[yi] for yi in y_pred]
        y_true = [ymap[yi] for yi in y_true]
        labels = [ymap[yi] for yi in labels]
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    cm_sum = np.sum(cm, axis=1, keepdims=True)
    cm_perc = cm / cm_sum.astype(float) * 100
    annot = np.empty_like(cm).astype(str)
    nrows, ncols = cm.shape
    for i in range(nrows):
        for j in range(ncols):
            c = cm[i, j]
            p = cm_perc[i, j]
            if i == j:
                s = cm_sum[i]
                annot[i, j] = '%.1f%%\n%d/%d' % (p, c, s)
            elif c == 0:
                annot[i, j] = ''
            else:
                annot[i, j] = '%.1f%%\n%d' % (p, c)
    cm = pd.DataFrame(cm, index=labels, columns=labels)
    cm.index.name = Actual
    cm.columns.name = Predicted
    fig, ax = plt.subplots(figsize=figsize)
    sn.heatmap(cm, annot=annot, fmt='', ax=ax, cmap='Blues')
    plt.savefig(filename)
    return 0

def main(argv):
    """main entry of the program"""
    global cor_d, c, d, df, test_d
    test_d = pd.merge(test_d, c[["SourceFile", "IsHuman"]], on = "SourceFile")
    test_d.IsHuman = test_d.IsHuman.apply(convert1)
    test_d.rename(columns = {"IsHuman" : "Classifer"}, inplace = True) 

    j = Json.Json("../Data/p1/", 0.5, 1)
    #j_hu = j.getHuImage

    #for cnn + mlp human classifier
    cm_analysis(test_d["actual"], test_d["Classifer"], "../Results/test_d_classifier_cm.png", [1, 0], ymap=None, figsize=(5,4))
    
    #for the BODY-25 model with different thresholds
    #j_hu = j.getHuImage(0.5, 2)
    #j_hu = pd.DataFrame(list(j_hu.items()), columns = ["SourceFile", "OpenPose"])
    #test_d_1 = pd.merge(test_d, j_hu, on = "SourceFile")
    #cm_analysis(test_d_1["actual"], test_d_1["OpenPose"], "../Results/test_d_openpose_cm_0.5_2.png", [1, 0], ymap=None, figsize=(5,4))
    
    j_hu = j.getHuImage(0.5, 1)
    j_hu = pd.DataFrame(list(j_hu.items()), columns = ["SourceFile", "OpenPose"])
    test_d_2 = pd.merge(test_d, j_hu, on = "SourceFile")
    cm_analysis(test_d_2["actual"], test_d_2["OpenPose"], "../Results/test_d_openpose_cm_0.5_1.png", [1, 0], ymap=None, figsize=(5,4))
    
    #j_hu = j.getHuImage(0.4, 1)
    #j_hu = pd.DataFrame(list(j_hu.items()), columns = ["SourceFile", "OpenPose"])
    #test_d_3 = pd.merge(test_d, j_hu, on = "SourceFile")
    #cm_analysis(test_d_3["actual"], test_d_3["OpenPose"], "../Results/test_d_openpose_cm_0.4_1.png", [1, 0], ymap=None, figsize=(5,4))
    
    #j_hu = j.getHuImage(0.4, 2)
    #j_hu = pd.DataFrame(list(j_hu.items()), columns = ["SourceFile", "OpenPose"])
    #test_d_4 = pd.merge(test_d, j_hu, on = "SourceFile")
    #cm_analysis(test_d_4["actual"], test_d_4["OpenPose"], "../Results/test_d_openpose_cm_0.1_1.png", [1, 0], ymap=None, figsize=(5,4))
    
    #save result in a csv file
    c.IsHuman = c.IsHuman.apply(convert1)
    re = df[["SourceFile", "CreateDate", "placeID", "h"]]
    re1 = c[["SourceFile", "human_prob", "non_human_prob", "IsHuman"]]
    result = pd.merge(re, re1, on = "SourceFile")
    result_d = pd.merge(result, j_hu, on = "SourceFile")
    result_d.CreateDate = result_d.CreateDate.str.replace(r"\s\s+", r" ")#remove extra spaces
    result_d.to_csv("../Results/results_d.csv", index = False)
    results_t = pd.merge(test_d_2, df[["SourceFile", "h"]], on = "SourceFile")
    results_t.to_csv("../Results/test_d_2.csv", index = False)
    
    df.CreateDate = df.CreateDate.str.replace(r"\s\s+", r" ")
    cm_re = pd.merge(test_d_2, df[["SourceFile", "placeID", "CreateDate"]], on = "SourceFile")
    cm_re.to_csv("../Results/cm_re.csv", index = False)
    #cm_re.loc[(cm_re["actual"] == 1) & (cm_re["OpenPose"] == 1)]
    #cm_re.loc[(cm_re["actual"] == 1) & (cm_re["OpenPose"] == 0)]
    hp_all = result_d.groupby(["placeID", "h"]).sum().reset_index()[["placeID", "OpenPose", "h"]]
    flights = hp_all.pivot("placeID", "h", "OpenPose")
    ax = sn.heatmap(flights, cmap="Blues")
    #ax.set_title('Time distribution of skeletons between different sites.\nColor represents the number of skeletons')
    figure = ax.get_figure()    
    figure.savefig('../Results/heatmap_h_id_huImage.png', dpi=400)

    hp_diff_d = result_d.loc[result_d["OpenPose"] != result_d["IsHuman"]]
    hp_diff_d["OpenPose"].replace({0: 1}, inplace=True)
    hp_diff = hp_diff_d.groupby(["placeID", "h"]).sum().reset_index()[["placeID", "OpenPose", "h"]]
    flights = hp_diff.pivot("placeID", "h", "OpenPose")

    ax = sn.heatmap(flights, cmap="Blues")
    #ax.set_title('Time distribution of skeletons between different sites.\nColor represents the number of skeletons')
    figure = ax.get_figure()   
    figure.savefig('../Results/heatmap_h_id_misclassified.png', dpi=400)
    return 0

if __name__ == "__main__":
    """Make sure the main function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)