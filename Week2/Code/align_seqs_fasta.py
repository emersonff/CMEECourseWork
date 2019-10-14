#!/usr/bin/env python3
"""Take the DNA sequences as an input from fasta files in ../Data/fasta directory and save the best alignment along with its corresponding score in a single 
text file to an appropriate location. 
"""
__appname__ = "align 2 DNA sequences"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.2"
__license__ = "none"

###imports
import sys

###global variables 
l1, l2, s1, s2= [0 for i in range(4)]# initialise all to 0

###functions
def init(f1 = open("../Data/fasta/407228326.fasta", "r"), f2 = open("../Data/fasta/407228412.fasta", "r")):
    """A fucntion that takes two files as in. Defualt files are ../Data/fasta/407228326.fasta and ../Data/fasta/407228412.fasta
    Assign the longer sequence s1, and the shorter to s2.
    l1 is length of the longest, l2 that of the shortest"""
    global l1, l2, s1, s2
    seq1 = f1.readline()#omit first line
    seq2 = f2.readline()
    seq1 = f1.read().replace("\n", "")#delete all new line characters
    seq2 = f2.read().replace("\n", "")
    f1.close()
    f2.close()
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
    """A function to find the best match(highest score) for the two sequences"""
    my_best_align = None
    my_best_score = -1

    for i in range(l1): # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2 # think about what this is doing! --------point out where is the start point
            my_best_score = z 
    print(my_best_align)
    print(s1)
    print("Best score:", my_best_score)
    print("writing result in ../Result/align_fasta_result.txt ...")
    f = open("../Result/align_fasta_result.txt", "w")
    f.write(my_best_align + "\n")
    f.write(s1 + "\n")
    f.write("Best score:" + str(my_best_score) + "\n")
    print("Finished!")


def main(argv):
    if(len(argv) >2):# if file names are specified by users
        f1 = open("../Data/fasta/" + argv[1], "r")# open file specified in first argument
        f2 = open("../Data/fasta/" + argv[2], "r")# open file specified in second argument
        init(f1, f2) 
    else:
        init()
    find_best()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)