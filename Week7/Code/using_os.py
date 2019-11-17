""" This is blah blah"""

# Use the subprocess.os module to get a list of files and  directories 
# in your ubuntu home directory 

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

import subprocess
import re

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:


# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []
FilesDirsStartingWithCc = []
DirsStartingWithCc = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'
    pattern = r"^[Cc].*" #start with C or c
    pattern2 = r"^C.*" #start with C
    #pattern = r".*"
    regex = re.compile(pattern)
    regex2 = re.compile(pattern2)
    for l in files:
        for match in regex.findall(l):
            #print(match)
            FilesDirsStartingWithCc.append(match)
        for match in regex2.findall(l):
            FilesDirsStartingWithC.append(match)

#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 
    pattern = r".*\/[Cc][^\/]*\/?"
    pattern2 = r".*\/[C][^\/]*\/?"
    #pattern = r".*"
    regex = re.compile(pattern)
    for match in regex.findall(dir):
        FilesDirsStartingWithCc.append(match)
        DirsStartingWithCc.append(match)
    regex = re.compile(pattern2)
    for match in regex.findall(dir):
        FilesDirsStartingWithC.append(match)