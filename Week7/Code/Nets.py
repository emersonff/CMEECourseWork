#!usr/bin/env python3
"""plots a directed graph in python"""
__appname__ = "Nets"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import csv
import sys
import scipy as sc
import networkx as nx 
import matplotlib.pyplot as p
import matplotlib.lines as mlines
###globals

###functions
def readfile(filename):
    """read data from csv file"""
    temp = []
    f = open(filename, "r")
    csvread = csv.reader(f)
    for row in csvread:
        temp.append(row)
    f.close()
    return temp

def AdjList(array):
    """returns an adjacency representing edges"""
    adj = []
    weight = []
    n = len(array) - 1 #6
    names = array[0, :] #names of nodes
    data = array[1:, :] #excluding names
    for i in range(n):#0-5
        n1 = names[i]
        for j in range(n):#0-5
            n2 = names[j]
            w = int(data[i,j])
            if w > 0:
                weight.append(w)
                adj.append([n1, n2])
    return adj, weight

def norm_weight(w):
    """scaling weights, used for width of edges."""
    temp = []
    #min_w = min(w)
    #max_w = max(w)
    temp = 1 + sc.array(w) / 10
    temp.tolist()
    return temp

def main(argv):
    """main entry point of the program"""
    global D_e, D_n, nodes, edges, weights, G
    #reads data from csv files
    D_e =sc.array(readfile("../Data/QMEE_Net_Mat_edges.csv"))
    D_n =sc.array(readfile("../Data/QMEE_Net_Mat_nodes.csv"))

    nodes = D_n[1 :, 0] # a ndarray stores nodes
    edges,weights = AdjList(D_e)
    pos = nx.circular_layout(nodes)#position nodes uniformly random
    color_map = ["blue","blue" ,"green", "green", "green", "red"]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges, weight = weights)
    nx.draw_networkx(G, pos, node_size = 1500, node_color = color_map, \
    with_labels = True, edge_color = "grey",\
    width = norm_weight(weights)) #draw graph
    patch = [] #legends
    patch.append(mlines.Line2D([], [], color = "blue",\
         label = "University", marker = "o", linestyle = "None", markersize = 13))
    patch.append(mlines.Line2D([], [], color = "green",\
         label = "Hosting Partner", marker = "o", linestyle = "None", markersize = 13))
    patch.append(mlines.Line2D([], [], color = "red", \
        label = "Non-hosing Partner", marker = "o", linestyle = "None", markersize = 13))
    p.legend(handles = patch, bbox_to_anchor=(0.8, 0.8))#plot legends
    p.savefig("../Results/Nets.svg", format = "svg") # save graphs
    p.close()
    return 0 

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)