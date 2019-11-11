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
K = 10000 
t = sc.linspace(0, 15, 1000) # 15 time scale divided into 1000 steps
R0 = 10
C0 = 5 
RC0 = sc.array([R0,C0])

### functions
def dCR_dt(pops, t = 0):
    """A fucntion returns the growth rate of consumer and resource population at any 
    given time step"""
    R = pops[0]
    C = pops[1]
    dRdt = r * R * (1 - R / K) - a * C * R
    dCdt = - z * C + e * a * C * R
    return sc.array([dRdt, dCdt])

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
    pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output= True)
    print(infodict["message"])

    #Create the PdfPages object to which we will save the pages
    with PdfPages("../Results/LV2.pdf") as pdf:
        #plot first figure
        plt.figure()
        plt.plot(t, pops[:, 0], "g-", label = "Resource density")#plot
        plt.plot(t, pops[:, 1], "b-", label = "Consumer density") # x, y, format, label
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
        plt.plot(pops[:, 0], pops[:, 1], "r-")
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
    print("The final resource population is: " + str(pops[-1, 0]))
    print("The final consumer population is: " + str(pops[-1, 1]))
    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)