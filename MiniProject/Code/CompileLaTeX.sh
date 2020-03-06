#!/bin/bash
#simple script to complie latex with bibtex
pdflatex $1.tex
pdflatex $1.tex
bibtex References
pdflatex $1.tex
pdflatex $1.tex
evince $1.pdf &

rm *~
rm *.aux
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg
rm *.nlo
