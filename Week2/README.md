# Week 2:Biological Computing in Python 1
In this week, all python files are assumed to run under ipyhton environment. Type `ipython` in terminal to enter ipython.

## Python Input/Output
In this section, all files are saved in [Sandbox](Sandbox) directory.
* [basic_io1.py](Code/basic_io1.py):
A python file that prints all the lines in [test.txt](Sandbox/test.txt) and then prints lines again without blank lines. To run:

    run basic_io1.py

* [basic_io2.py](Code/basic_io2.py):
A python file that save each element in `range(100)` on a seperate line in [testout.txt](Sandbox/testout.txt). To run:

    run basic_io2.py

* [basic_io3.py](Code/basic_io3.py):
A python file using `pickle` package to save a dictionary to [testp.p](Sandbox/testp.p), Then it will load the dictionary from the file and print it. To run:

    run basic_io3.py

## Shell Scripting
* [boilerplate.sh](Code/boilerplate.sh): 

A simple bash script that print "This is a shell script!" in ternimal. To run it, simply type down the following command in the terminal:

    bash boilerplate.sh

* [tabtocsv.sh](Code/tabtocsv.sh):

A script to convert a tab separated file into a **c**omma **s**eparated **v**alues file. It is saved as a different named file. To run:

    bash tabtocsv.sh file_name


* [variables.sh](Code/variables.sh):

A script to show how to accept inputs from terminal. To run:

    bash variables.sh

* [MyExampleScript.sh](Code/MyExampleScript.sh):

A script to show how to print variables. To run:

    bash MyExampleScript.sh

* [CountLines.sh](Code/CountLines.sh):


A simple bash script that count the line numbers of a given file. To run:

    bash CountLines.sh file_name

* [ConcatenateTwoFiles.sh](Code/ConcatenateTwoFiles.sh):

A script to concatenate two files into a single file. The first two arguments should specify which files will be merged and the third argument specifies the merged file. To run:

    bash ConcatenateTwoFiles.sh first_file second_file merged_file

* [tiff2png.sh](Code/tiff2png.sh):

A script to convert all .tif files in current directory into .jpg files. This script assumes that you have already done ```sudo apt install imagemagick```. To run:

    bash tiff2png.sh

* [csvtospace.sh](Code/csvtospace.sh):

This script takes a **c**omma **s**eparated **v**alues and converts it to a space separated values file and saves it as a different named file in current directory. The user should not To run:

    bash csvtospace.sh csv_file

## Version control with Git
Added .gitgnore file and README.md file.

## Scientific documents with LaTeX
* [CompileLaTeX.sh](Code/CompileLaTeX.sh):

A script that automatically compiles a latex file. It also adds citations and create a `.pdf` file as well as delete any redundant files. To compile [FirstExample.tex](Code/FirstExample.tex):

    bash CompileLaTeX.sh FirstExample