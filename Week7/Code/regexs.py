#!usr/bin/env python3
"""regular expression in python"""
__appname__ = "regexs"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import re

#globals
my_string = "a given string"
match = re.search(r"\s", my_string)
print(match)
match = re.search(r"\d", my_string)# none cause no numeric characters
print(match)
MyStr = "an example"
match = re.search(r"\w*\s", MyStr)
if match:
    print("found a match:", match.group())
else:
    print("did not find a match")

match = re.search(r"2", "it takes 2 to tango")
match.group()

match = re.search(r"\d", "it takes 2 to tango")
match.group()

match = re.search(r'\d.*' , "it takes 2 to tango")
match.group()

match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

match = re.search(r'\s\w*$', 'once upon a time')
match.group()

re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()

re.search(r'^\w*.*?\s', 'once upon a time').group()

re.search(r'<.+>', 'This is a <EM>first</EM> test').group()

re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()
re.search(r'\d*\.?\d*','1432.75+60.22i').group()

re.search(r'\s+[A-Z]\w+\s*\w+', "The bird-shit frog's name is Theloderma asper.").group()

MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s]+", MyStr)
match.group()

MyStr = 'Samraat Pawar, s-pawar@imperial.ac.uk, Systems biology and ecological theory'

match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s&]+",MyStr)
match.group()