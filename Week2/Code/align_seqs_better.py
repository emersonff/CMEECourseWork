#!/usr/bin/env python3
"""Take the DNA sequences as an input from a signal external file and save the best alignment along with its corresponding score in a single 
text file to an appropriate location. No external input should be required.
"""
__appname__ = "align 2 DNA sequences"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.2"
__license__ = "none"

###imports
import sys
import pickle

###global variables 
l1, l2, s1, s2= [0 for i in range(4)]# initialise all to 0

###functions
def init():
    """A fucntion that read DNA sequences from an external file.
    Assign the longer sequence s1, and the shorter to s2.
    l1 is length of the longest, l2 that of the shortest"""
    global l1, l2, s1, s2
    f = open("../Data/seqs.txt", "r") # a single file that stores each sequence on a separate line
    seq1 = f.readline() #"ATCGCCGGATTACGGG\n"
    seq2 = f.readline() #"CAATTCGGAT\n"
    f.close() 
    seq1 = seq1[:-1]##get characters from position 0 to position n-1 #omit new line character
    seq2 = seq2[:-1]
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths

def calculate_score(s1, s2, l1, l2, startpoint):
    """A function that comoutes a score by returning the number of matches
    starting from arbitrary startpoint(chosen by user)"""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched) #print matched expression          
    print("." * startpoint + s2)      #print shorter sequence
    print(s1)                         #print longer sequence
    print(score)                      #print score
    print(" ")                        #new line

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

def find_best():
    """A function to find all best matches(highest score) for the two sequences and save them to Result directory in align_result.txt"""
    #my_best_align = None
    my_best_score = -1
    txt = []
    index = []
    f = open("../Result/align_result.p","wb")
    for i in range(l1): # store all scores in index list
        z = calculate_score(s1, s2, l1, l2, i)
        index.append(z)
    my_best_score = max(index) # highest score
    for i in range(l1):
        if index[i] == my_best_score:
            txt.append("." * i + s2) ##append the best align to txt list
    pickle.dump(txt, f)
    f.close()
    print("All best results has been recorded in ../Result/align_result.p")
    f = open("../Result/align_result.p","rb")
    best = pickle.load(f)
    f.close()
    print(best)
    #print(index)
    #print(my_best_align)
    #print(s1)
    #print("Best score:", my_best_score)


def main(argv):
    init()
    find_best()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)