#!/usr/bin/env python3
"""python exercise dictionary.py"""
# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

__appname__ = "dicitonary"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__="0.0.1"
__license__="none"

###global variables
taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

taxa_dic = {}#initialise

###functions
def pop_dic():
        global taxa, taxa_dic #global variables declaration


        return 0

def main(argv):
        pop_dic()
        print(str(taxa_dic))
        return 0

if __name__ == "__main__":
        """make sure the main function is called from command line"""
        status = main(sys.argv)
        sys.exit(status)