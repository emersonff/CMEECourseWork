#!usr/bin/env python3
"""Python version of Vectorize2.R.  Runs the stochastic (with gaussian fluctuations) Ricker Eqn """
__appname__ = ""
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"
###imports
import sys
import numpy as np
import time

### globals
np.random.seed(1)# set random seed
#np.random.uniform(low = 0.5, high = 1.5, size = 1000) #draw samples form a uniform distribution over the interval [0.5, 1.5).



###functions
def stochrickvect(p0=np.random.uniform(0.5, 1.5, 1000),r=1.2,K=1,sigma=0.2,numyears=100):
    """ stochastic Ricker model implemented in python.
The default value of parameter p0 is A python list of 1000 samples from a unifrom distribution over interval [0.5, 1.5)"""
    N = np.zeros((numyears,len(p0))) #array of size numyears * len(p0) filled with 0
    N[0, :] = p0 #set first row
    for yr in range(1,numyears):
        N[yr, :] = N[yr - 1, :] * np.exp(r * (1 - N[yr - 1, :] / K)+np.random.normal(0, sigma, 1))# normal distribution(mean, sd, size)
    return N

def main(argv):
    """main entry point of the prgram"""
    start_v = time.time()
    stochrickvect()
    end_v = time.time()
    print("Python version of Stochastic Ricker takes:")
    print(end_v - start_v)
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)