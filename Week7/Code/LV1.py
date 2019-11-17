#!usr/bin/env python3
"""Numerical integration in Python for solving a classical model in biology
 — the Lotka-Volterra model for a predator-prey system in two-dimensional space """
__appname__ = "LV1.py"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

### imports
import sys
import scipy as sc
import scipy.integrate as integrate
import matplotlib.pylab as p
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

### globals
r = 1. #intrinsic growth rate of the resource population
a = 0.1 # per-captia search rate for the resource multiplied by its attack success probability
z = 1.5 # mortality rate
e = 0.75 # consumer's efficiency in converting resources to consumer biomass
t = sc.linspace(0, 15, 1000) # 15 time scale divided into 1000 steps
R0 = 10 #initial resource population abundance
C0 = 5 # initial comsumer population abundance
RC0 = sc.array([R0,C0])

### functions
def dCR_dt(pops, t = 0):
    """A fucntion returns the growth rate of consumer and resource population at any 
    given time step"""
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * C * R
    dCdt = - z * C + e * a * C * R
    return sc.array([dRdt, dCdt])

def main(argv):
    """main entry point of the program"""
    #take arguments from command line
    global r, a, z, e
    if len(argv) >= 2: r = argv[1]
    elif len(argv) >= 3: a = argv[2]
    elif len(argv) >= 4: z = argv[3]
    elif len(argv) >= 5: e = argv[4]

    #infodict is a dictionary contains information about the integration
    pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output= True)
    print(infodict["message"])

    #Create the PdfPages object to which we will save the pages
    with PdfPages("../Results/LV_model.pdf") as pdf:
        #plot first figure
        plt.figure()
        plt.plot(t, pops[:, 0], "g-", label = "Resource density")#plot
        plt.plot(t, pops[:, 1], "b-", label = "Consumer density") # x, y, format, label
        plt.grid() #configure the grid lines
        plt.legend(loc = "best") # best place the legend with minimum overlap with other drawn artists
        plt.xlabel("Time")
        plt.ylabel("Population density")
        plt.title("Consumer-Resource population dynamics")
        pdf.savefig() #save the current figure into a pdf page
        plt.close()
        #plot second figure
        plt.figure()
        plt.plot(pops[:, 0], pops[:, 1], "r-")
        plt.grid()
        plt.xlabel("Resource density")
        plt.ylabel("Consumer density")
        plt.title("Consumer-Resource population dynamics")
        pdf.savefig()#save figure
        plt.close()

    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)