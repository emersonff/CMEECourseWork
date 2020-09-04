#!usr/bin/env python3
"""Kp class to read skeleton data"""
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



class Kp:
    """class Kp"""

    def __init__(self, p):#constructor
        """constructor"""
        #self.placeID = id# place id
        self.pts = [[p[i], p[i+1]] for i in np.array(range(0,45,3))]# x,y coordinates for 15 points
        self.limbs = np.array([(self.pts[0], self.pts[1]), (self.pts[1], self.pts[2]), (self.pts[2], self.pts[3]), (self.pts[3], self.pts[4]), \
                      (self.pts[1], self.pts[5]), (self.pts[5], self.pts[6]), (self.pts[6], self.pts[7]), (self.pts[1], self.pts[8]), \
                      (self.pts[8], self.pts[9]), (self.pts[9], self.pts[10]), (self.pts[10], self.pts[11]), (self.pts[8], self.pts[12]), \
                      (self.pts[12], self.pts[13]), (self.pts[13], self.pts[14])])
        self.adj = self.__AdjMatrix()# adjency matrix
        self.d = self.__DeMatrix()# degree matrix
        self.Lap = self.d - self.adj#the Laplacian matrix
        self.Lap2 = self.__NormLpMatrix()
        self.spec = self.__SpecMatrix()
        self.fv = self.__Fv()

    def __getAngle(self, l1, l2):
        """return the angle between 2 limbs"""
        a = 0
        if np.all(l1[1] == l2[0]):
            v1 = l1[0] - l1[1]
            v2 = l2[0] - l2[1]
        elif np.all(l1[0] == l2[1]):
            v1 = l1[1] - l1[0]
            v2 = l2[1] - l2[0]
            #v1 = l1[0] - l1[1]
            #v2 = l2[0] - l2[1]           
        else:
            return "n"
        a = np.arccos(np.clip(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)),-1.0,1.0))
        #np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        return a

    def __AdjMatrix(self):
        m = np.zeros((14, 14))
        for i in np.array(range(0,14)):
            for j in np.array(range(0,14)):
                a = self.__getAngle(self.limbs[i], self.limbs[j])
                if type(a) != str:
                    m[i][j] = np.exp(a)
                    #m[i][j] = a
        return m
    
    def __DeMatrix(self): 
        return np.diag(self.adj.sum(axis=1))

    def __NormLpMatrix(self):
        """get the normalised Laplacian matrix"""
        try:
            x, V = np.linalg.eig(self.Lap)
        except:
            print(self.Lap) 
        x = abs(x)
        x = zip(x, range(len(x)))
        x = sorted(x, key=lambda x:x[0])#(eigenvalue, index) sorted in ascending order
        U = np.array([V[i] for (v,i) in x[:14]]).T
        A = np.diag([v for (v, i) in x])
        return U @ A @ U.T

    def __SpecMatrix(self):
        """get the Spectral matrix"""
        x, V = np.linalg.eig(self.Lap)
        x = abs(x)
        x = zip(x, range(len(x)))
        x = sorted(x, key=lambda x:x[0])#(eigenvalue, index) sorted in ascending order
        U = np.array([V[i] for (v,i) in x[:14]])
        return np.array([np.sqrt(x[i][0]) * U[i] for i in np.array(range(0,14))]).T

    
    def __Fv(self):
        """calculate the elementary symmetric polynomials using the 
        Newton-Girard formula"""
        #esp =[]
        i = 13
        col = [row[i] for row in self.spec]
        #power symmetric polynomials
        P = [np.sum(np.power(col, i + 1)) for i in np.array(range(0,14))]
        S = []
        S.append(1)
        S.append(np.sum(col))
        for r in np.array(range(2,15)):
            s = (((-1) ** (r + 1)) / r) * sum([((-1) ** (k + r)) * P[k - 1] * S[r - k] for k in np.array(range(1,len(S) + 1))])
            S.append(s)
        #esp.append(S[1:])
        return S[1:]