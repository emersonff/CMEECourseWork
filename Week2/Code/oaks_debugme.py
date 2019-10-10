#!/usr/bon/env python3
"""finds all oaks in TestOakData.csv file and records them in JustOakData.csv file."""
import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak("Quercuss")
    False

    >>> is_an_oak("Quercus robur")
    True
    """
    return name.lower().startswith('quercus ')

def main(argv): 
    f = open('../Data/trees.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    
    f.close()
    g.close()
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

#doctest.testmod() run on the fly using command python -m doctest -v oaks_debugme.py