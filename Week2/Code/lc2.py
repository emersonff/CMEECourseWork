#!/usr/bin/env python
"""lc2"""
# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 
__appname__ = "lc2"
__author__ = "Xiang Li"
__version__ = "0.0.1"
__license__ = "none"

###imports
import sys

### global variables
# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

###functions
def lc():
    """create and print lists of tuples using list comprehensions"""
    global rainfall
    g_100 = [(i[0], i[1]) for i in rainfall if i[1] >100]
    l_50 = [i[0] for i in rainfall if i[1] < 50]
    print("greater than 100ml: " + str(g_100))
    print("less than 50ml: " + str(l_50))
    return 0

def loops():
    """create and print lists of tuples using conventional loops"""
    global rainfall
    g_100 = []
    l_50 = []
    for i in rainfall:
        if i[1] > 100:
            g_100.append((i[0], i[1]))
        elif i[1] < 50:
            l_50.append(i[0])
    print("greater than 100ml: " + str(g_100))
    print("less than 50ml: " + str(l_50))
    return 0

def main(argv):
    """main function"""
    lc()
    print("\n")
    loops()
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
