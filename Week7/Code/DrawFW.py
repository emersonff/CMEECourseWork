#!usr/bin/env python3
"""generate a random adjacency list of food web
    with "connectance probability" in python"""
__appname__ = "DrawFW"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import networkx as nx 
import scipy as sc 
import matplotlib.pyplot as p 
import sys
from matplotlib.backends.backend_pdf import PdfPages
###globals
sc.random.seed(0)
MaxN = 30 # number of species
C = 0.75 # connectance
#p.switch_backend("Qt4Agg")
###functions
def GenRdmAdjList(N = 2, C = 0.5):
    """generate a random adjacency list of a N-species food web
    with "connectance probability" C: the probability of having a link
    between any pair of species in the food web.
    The two columns of numbers correspond to the consumer and resource ids, respectively."""
    Ids = range(N)
    ALst = []
    for i in Ids:
        if sc.random.uniform(0,1,1) < C:
            Lnk = sc.random.choice(Ids, 2).tolist()
            if Lnk[0] != Lnk[1]: #avoid self loops (cannibalistic)
                ALst.append(Lnk)
    return ALst # ALst[:, 0] consumer ids       ALst[:, 1] resource ids


def main(argv):
    """main entry of the program"""
    global Sizs
    AdjL = sc.array(GenRdmAdjList(MaxN, C))
    #print(AdjL)
    Sps = sc.unique(AdjL)# get species ids
    SizRan = [-10, 10] # body size range  using log10 scale because it is log-normally distributed
    Sizs = sc.random.uniform(SizRan[0], SizRan[1], MaxN)
    #print(Sizs)
    p.hist(Sizs)#log10 scale histogram
    p.hist(10 ** Sizs) # raw scale
    p.close("all")
    pos = nx.circular_layout(Sps) # position nodes on a circle
    G = nx.Graph() # base class for undirected graph
    G.add_nodes_from(Sps)#add nodes and links
    G.add_edges_from(tuple(AdjL))
    #node size that are proportional to (log) body size.
    NodSizs = 1000 * (Sizs - min(Sizs)) / (max(Sizs) - min(Sizs))
    with PdfPages("../Results/DrawFW.pdf") as pdf:
        nx.draw_networkx(G, pos, node_size = NodSizs) # render(plot) the graph
        pdf.savefig()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
