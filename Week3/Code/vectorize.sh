#!/bin/bash
#  Author: XIang Li xl15918@ic.ac.uk
# Script: vectorize.sh
# Desc: run four vectorize scirpts and compare the computational speed
# Arguments: non
# Date: Oct 2019

echo "running Vectorize1.py..."
python3 Vectorize1.py
echo
echo "running Vectorize2.py..."
python3 Vectorize2.py
echo
echo "running Vectorize1.R..."
Rscript Vectorize1.R
echo
echo "running Vectorize2.R..."
Rscript Vectorize2.R