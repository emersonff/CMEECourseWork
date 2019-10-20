#!/usr/bin/env python3
#Filename: using_name.py
"""A python program to show the difference between running a program and importing it as a module. """
if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I`m being imported from another module")

print("This module name is " + __name__)