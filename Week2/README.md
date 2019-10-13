# Week 2:Biological Computing in Python 1
all python files listed below are assumed to run under ipyhton environment. Type `ipython` in terminal to enter ipython. using `python` command to run python script if you want to run from bash ternimal.

## Python Input/Output
* [basic_io1.py](Code/basic_io1.py):
A python file that prints all the lines in [test.txt](Sandbox/test.txt) and then prints lines again without blank lines. To run:

```
run basic_io1.py
```

* [basic_io2.py](Code/basic_io2.py):
A python file that save each element in `range(100)` on a seperate line in [testout.txt](Sandbox/testout.txt). To run:

```
run basic_io2.py
```

* [basic_io3.py](Code/basic_io3.py):
A python file using `pickle` package to save a dictionary to [testp.p](Sandbox/testp.p), Then it will load the dictionary from the file and print it. To run:

```
run basic_io3.py
```

### Handling  `CSV` Files
* [basic_csv.py](Code/basic_csv.py):
Reads [testcsv.csv](Data/testcsv.csv) in [Data](Data) directory and prints each species name on a seprate line. Then writes a file [bodymass.csv](Data/bodymass.csv) containing only species name and Body mass. And then prints [bodymass.csv](Data/bodymass.csv). To run:

```
run basic_csv.py
```

## Control Flows Tools
### Conditionals
* [cfexercises1.py](Code/cfexercises1.py):
A python file demonstrates how to use conditional statements. It has been modified into functions which accept parameter(s) and return corresponding value(s). The main function contains servral call instances. To run:  
```
run cfexercises1.py
```

### Loops
* [loops.py](Code/loops.py):

### Loops and Conditional Combined
* [cfexercises2.py](Code/cfexercises2.py):

## Comprehensions