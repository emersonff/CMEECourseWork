#!bin/bash
#count the number of lines in a file
NumLines=`wc -l < $1`
echo "THe file $1 has $NumLines lines"
echo
