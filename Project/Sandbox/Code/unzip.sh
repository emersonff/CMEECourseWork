#!/bin/bash
# Author: Xiang Li xl15918@ic.ac.uk
# Script: unzip.sh
# Desc: unzip all zip files. Change the path to the zip file and output directory accordingly.
# Arguments: none
# Date: May 2020
for zip in *.zip
do
zip -s- $zip -O ../merged/$zip
unzip ../merged/$zip -d ~/Pic
done
