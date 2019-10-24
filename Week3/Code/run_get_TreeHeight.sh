#!/bin/bash
#  Author: XIang Li xl15918@ic.ac.uk
# Script: run_get_TreeHeight.sh
# Desc: tests get_TreeHeight.R. Include trees.csv as example file
# Arguments: non
# Date: Oct 2019

echo "Running get_TreeHeight.R..."
Rscript get_TreeHeight.R ../Data/trees.csv
echo ""
echo "Running get_TreeHeight.py..."
python3 get_TreeHeight.py ../Data/trees.csv