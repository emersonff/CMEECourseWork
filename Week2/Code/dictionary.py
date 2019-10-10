#!/usr/bin/env python3
"""python exercise dictionary.py"""
# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

__appname__ = "dicitonary"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"
###imports
import sys

###global variables
taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia'),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ] #list of tuples

taxa_dic = {}#initialise

###functions
def pop_dic():
        """function to populate a dicitonary and store it in global variable taxa_dic"""
        #global taxa, taxa_dic #global variables declaration
        for i in range(len(taxa)):
                taxa_dic[taxa[i][1]] = set()## set all keys and initiallise all values to empty sets
        for i in range(len(taxa)):
                taxa_dic[taxa[i][1]].add(taxa[i][0])## iterate the list and add values to the corresponding sets according to the kay names
        return 0

def main(argv):
        """main entry point to the program"""
        pop_dic()
        print(str(taxa_dic))
        return 0

if __name__ == "__main__":
        """make sure the main function is called from command line"""
        status = main(sys.argv)
        sys.exit(status)