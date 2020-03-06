#!/bin/bash
if [ $# -eq 0 ]
then
echo "No input files."
else
f=`basename $1 |cut -f 1 -d "."`
pdflatex $f
pdflatex $f
biber References
pdflatex $f
pdflatex $f
#move to Results
mv ./$f.pdf ../Results/ 
evince ../Results/$f.pdf &

##Cleanup
rm *~
rm *.aux
rm *.xml
rm *.bcf
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg
rm *.pdf
fi
