#!/usr/bin/env python3
"""Some functions exemplifying the use of  control statements"""

__appname__="[application name here]"
__author__="Xiang Li(xiang.li419@imperial.ac.uk)"
__version__="0.0.1"
__license__="License ofr this code"

##imports ##
import sys #module to interface our program with the operating system
import doctest # import the doctest module

##constants##

##functions##
def even_or_odd(x=0): #if not specifed, x should take vavlue 0
    """Find whether a number x is even or odd.

    >>> even_or_odd(10)
    '10 is Even'

    >>> even_or_odd(5)
    '5 is Odd'

    whenever a float is provided, then the closest integer is used:
    >>> even_or_odd(3.2)
    '3 is Odd'

    in the case of negative numbers, the positive is taken:
    >>> even_or_odd(-2)
    '-2 is Even'

    """

    #define function to be tested
    if x % 2 == 0:
        return "%d is Even" %x
    return "%d is Odd" %x

def largest_divisor_five(x=120):
    """Find which is the largest divisor of x among 2,3,4,5."""
    largest = 0
    if x % 5 == 0:
        largest = 5
    elif x % 4 == 0:
        largest = 4
    elif x % 3 == 0:
        largest = 3
    elif x % 2 == 0:
        largest = 2
    else:
        return "No divisor found for %d" %x
    return "The largest divisor of %d is %d" %(x, largest)

def is_prime(x=70):
    """Find whether an integer is prime"""
    for i in range(2, x):
        if x % i == 0:
            print("%d is not a prime, %d is a divisor" %(x, i))
            return False
    print("%d is a prime" %x)
    return True

def find_all_primes(x=22):
    """Find all the primes up to x"""
    allprimes = []
    for i in range(2, x + 1):
        if is_prime(i):
            allprimes.append(i)
        print("There are %d primes between 2 and %d" %(len(allprimes), x))
    return allprimes
 

####### I SUPPRESSED THIS BLOCK: WHY? #######

# def main(argv): 
#     print even_or_odd(22)
#     print even_or_odd(33)
#     return 0

# if (__name__ == "__main__"):
#     status = main(sys.argv)
############################################

doctest.testmod()
#python -m doctest -v your_function_to_test.py
# run doctest on the fly
