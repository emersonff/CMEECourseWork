#!/bin/bash
#  Author: XIang Li xl15918@ic.ac.uk
# Script: runMe.R
# Desc: run four vectorize scirpts and compare the computational speed
# Arguments: non
# Date: Feb 2020

echo "Running DataPrep.py..."
python3 DataPrep.py
echo
echo "Running Fitting.R..."
Rscript Fitting.R
echo
echo "Running Plotting.R..."
Rscript Plotting.R
echo
echo "Compling tex file..."
sh CompileLaTex.sh Report
