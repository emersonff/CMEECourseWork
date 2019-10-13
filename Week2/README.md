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
A python file demonstrates how to use conditional statements. It has been modified into functions which accept parameter(s) and return corresponding value(s). The `main` function contains servral instances of function call. To run:  

```
run cfexercises1.py
```

### Loops
* [loops.py](Code/loops.py):
A python script demonstrates how to use for-loop and while-loop. It includes:
  * a for-loop to print numbers form 0 to 4
  * a for-loop to print all elements in `my_list` list
  * a for-loop to count the sum of all elements in `summands` list
  * a while-loop to print numbers from 0 to 99
  * a infinite while-loop.  
To run:

```
run loops.py
```

### Loops and Conditional Combined
* [cfexercises2.py](Code/cfexercises2.py):
A python script demonstrates how to combine condiitonal statements with loops. To run:

```
run cfexercises2.py
```

## Comprehensions
* [oaks.py](Code/oaks.py):
A python script demonstrates how to use list comprehensions in python. To run:

```
run oaks.py
```

## Variable Scope

## Writing Python Programs
* [boilerplate.py](Code/boilerplate.py):
A python program that prints a string if run it as a program(call `main` function). To run:
```
run boilerplate.py
```

### Components of the Python Program
#### the Docstring
* Docstring of [boilerplate.py](Code/boilerplate.py) can be accessed by:
```python
import boilerplate
help(boilerplate)
```

#### Why include __name__ == "__main__" and all that jazz
* [using_name.py](Code/using_name.py):
A python program to show the difference between running a program and importing it as a module. To run:
```
run using_name.py
```
Or to import it as a module:
```python
import using_name
```

#### What is `sys.argv`
* [sysargv.py](Code/sysargv.py):
A python program that prints the name of the program, the length of `sys.argv` and all the arguments including program name. To run:
```
run sysargv.py [var1, var2 ..]
```

### A Program with Control-flows Example
* [control_flow.py](Code/control_flow.py):
An example of a script that uses various control flow tools within a standard python program structure. It has four functions:
```python
even_or_odd(x = 0) #Find whether a number x is even or odd.
largest_divisor_five(x = 120) #Find which is the largest divisor of x among 2,3,4,5.
is_prime(x = 70) #Find whether an integer is prime
find_all_primes(x = 22) #Find all the primes up to x
```
To run it as a program:
```
run control_flow.py
```

## Practicals
* [lc1.py](Code/lc1.py):

A python program that is able to using list comprehensions or conventional loops to write three different
 lists containing the latin names, common names and mean body masses for
 each species in `birds`, respectively.  
 It contains 2 functions.`lc()` prints those three lists created using list comprehensions. And `loops()` prints lists
 created by conventional loops. The `main` function invokes both functions. To run:
```
run lc1.py
```
Or to import it as a module:
```python
import lc1
lc1.lc()
lc1.loops()
```

* [lc2.py](Code/lc2.py):

A python program that is able to using list comprehensions or conventional loops to create a list of month,rainfall tuples where
 the amount of rain was greater than 100 mm and a list of just month names where the
 amount of rain was less than 50 mm.  
 It also contains `lc()` and `loops()` functions. The `main` function invokes both. To run:
```
run lc2.py
```
Or to import it as a module:
```python
import lc2
lc2.lc()
lc2.loops()
```

* [dictionary.py](Code/dictionary.py):

A python program that populates a dictionary called `taxa_dic` derived from `taxa` so that it maps order names to sets of taxa. 
E.g. `'Chiroptera' : set(['Myotis lucifugus'])` etc. To run:
```
run dictionary.py
```

* [tuple.py](Code/tuple.py):

A python program that is able to print each element in a tuple called `birds` on a separate line using for-loop or `sep` operator.  
The `main` function invokes both `print_loop()` and `print_sep()`. To run:
```
run tuple.py
```
Or to import it as a module:
```python
import tuple
tuple.print_loop() #print every tuple on a separate line using a for loop
tuple.print_sep() #print every tuple on a separate line using * and sep operator
```

## Error in Your Python Code
### Unit Testing
#### Unit Testing with `doctest`


## Functions, Modules, and Code Compartmentalization

## Practicals
