#!/bin/bash
#merge two files into a new file
cat $1 > $3
cat $2 >> $3
echo "Merge File is"
cat $3
