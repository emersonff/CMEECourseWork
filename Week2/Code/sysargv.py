#!/usr/bin/env python3
"""A python program that prints the name of the program, the length of sys.argv and all the arguments including program name"""
import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
