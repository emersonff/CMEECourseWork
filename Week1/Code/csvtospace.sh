#!/bin/bash
#replace all the commas with spaces

cat $1|tr -s "," " " >> $1.txt

