#!/usr/bin/env python3
"""A python script containing a ZeroDivisionError error."""
def createabug(x):
    y = x**4
    z = 0
    ##import ipdb; ipdb.set_trace()
    y = y/z
    return y

createabug(25)  