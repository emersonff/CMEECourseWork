#!usr/bin/env python3
"""numerical computing in python"""
__appname__ = "LV2"
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
r = 1. 
a = 0.1
z = 1.5
e = 0.75
K = 30
t = sc.linspace(0, 15, 40) # 1000
R0 = 10
C0 = 5 
RC0 = sc.zeros((2,len(t)))#preallocate array
RC0[0, 0] = R0
RC0[1, 0] = C0

### functions
def CR(pops, t = 1):
    """A fucntion returns consumer and resource population abundances at all time steps"""
    for i in range(1, t):
        Rt = pops[0, i - 1]
        Ct = pops[1, i - 1]
        pops[0, i] = Rt * (1 + r *(1 - Rt / K) - a * Ct) #R
        pops[1, i] = Ct * (1 - z + e * a * Rt) #C
    return pops

def main(argv):
    """main entry point of the program"""
    #take arguments from command line
    global r, a, z, e, K
    if len(argv) >= 2: r = float(argv[1])
    if len(argv) >= 3: a = float(argv[2])
    if len(argv) >= 4: z = float(argv[3])
    if len(argv) >= 5: e = float(argv[4])
    if len(argv) >= 6: K = float(argv[5])
    #infodict is a dictionary contains information about the integration
    pops = CR(RC0, len(t))

    #Create the PdfPages object to which we will save the pages
    with PdfPages("../Results/LV3.pdf") as pdf:
        #plot first figure
        plt.figure()
        plt.plot(t, pops[0, :], "g-", label = "Resource density")#plot
        plt.plot(t, pops[1, :], "b-", label = "Consumer density") # x, y, format, label
        plt.grid() #configure the grid lines
        plt.legend(loc = "best") # best place the legend with minimum overlap with other drawn artists
        plt.xlabel("Time")
        plt.ylabel("Population density")
        plt.title("Consumer-Resource population dynamics")
        plt.figtext(0.85,0.9, "r = " + str(r))
        plt.figtext(0.85,0.8, "a = " + str(a))
        plt.figtext(0.85,0.7, "z = " + str(z))
        plt.figtext(0.85,0.6, "e = " + str(e))
        plt.figtext(0.85,0.5, "K = " + str(K))
        pdf.savefig() #save the current figure into a pdf page
        plt.close()
        #plot second figure
        plt.figure()
        plt.plot(pops[0, :], pops[1, :], "r-")
        plt.grid()
        plt.xlabel("Resource density")
        plt.ylabel("Consumer density")
        plt.title("Consumer-Resource population dynamics")
        plt.figtext(0.85,0.9, "r = " + str(r))
        plt.figtext(0.85,0.8, "a = " + str(a))
        plt.figtext(0.85,0.7, "z = " + str(z))
        plt.figtext(0.85,0.6, "e = " + str(e))
        plt.figtext(0.85,0.5, "K = " + str(K))
        pdf.savefig()#save figure
        plt.close()

    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)