# Week 3: Biological Computing in R and Data Management, Exploration and Visualization
all R script can be run using  `source()` under **Rstudio** environment or using `Rscript` command in bash ternimal.

## Biological Computing in R
In this chapter, We learned basic senmantics of R, R data structures and how to write and execute R script etc.

* [basic_io.R](Code/basic_io.R): A simple script to illustrate R input-output.   
* [control_flow.R](Code/control_flow.R): Demonstrates how to use conditional statements.   
* [break.R](Code/break.R): How to break out of a loop.   
* [next.R](Code/next.R): How to skip to next iteration of a loop.   
* [boilerplate.R](Code/boilerplate.R): boilerplate of R script.   
* [TreeHeight.R](Code/TreeHeight.R): calculates heights of trees and save the results in `TreeHts.csv`   
* [Vectorize1.R](Code/Vectorize1.R): sum all elements in a matrix.   
* [preallocate.R](Code/preallocate.R): How to preallocate a matrix to seed up.   
* [apply1.R](Code/apply1.R): How to use `apply` function.   
* [apply2.R](Code/apply2.R): How to use `apply` function.   
* [sample.R](Code/sample.R): Sampling using loops, `lapply` and `sapply`.   
* [Ricker.R](Code/Ricker.R): The Ricker model.   
* [Vectorize2.R](Code/Vectorize2.R): Vectirization version of the stochastic Ricker model.   
* [Vectorize1.py](Code/Vectorize1.py): python version of Vectorize1.R.   
* [Vectorize2.py](Code/Vectorize2.py): python version of Vectorize2.R.   
* [vectorize.sh](Code/Vectorize.sh): run 4 vectorize script and compare running time.   
* [try.R](Code/try.R): How to suppress any error messages using `try`.   
* [browse.R](Code/browse.R): How to enter brower mode for debugging using `browser()`.   
* [TAutoCorr.R](Code/TAutoCorr.R): Practical Autocorrelation in weather.   
* [get_TreeHeight.R](Code/get_TreeHeight.R): Calculates tree heights using a csv file as input and save the results.   
* [get_TreeHeight.py](Code/get_TreeHeight.py): python version of get_TreeHeight.R.   
run_get_TreeHeight.sh: tests get_TreeHeight.R and get_TreeHeight.py

## Data Management, Exploration and Visualization
In this chapter, We learned how to do data wrangling and how to visualise data using `ggplot2` package.

* [DataWrang.R](Code/DataWrang.R): A script demonstrate how to transfrom data into long format(data wrangling).  
* [DataWrangTidy.R](Code/DataWrangTidy.R): A script uses `dplyr` and `tidyr` for the same data wrangling steps.  
* [SQLinR.R](Code/SQLinR.R): Database in R.  
* [PP_Lattice.R](Code/PP_Lattice.R): script that draws and saves three lattice graphs by feeding interaction type and save plots in pdf format.  
* [Girko.R](Code/Girko.R): Plotting two dataframes.  
* [MyBars.R](Code/MyBars.R): How to annotate a plot.  
* [plotLin.R](Code/plotLin.R): annotating a plot.  
* [PP_Regress.R](Code/PP_Regress.R): draws regression line and points for all Feeding type * life stage category. Saves the analysis results in `.csv` file.  
* [PP_Regress_loc.R](Code/PP_Regress_loc.R): Similar to PP_Regress.R. Using Type.of.feeding.interaction, Predator.lifestage, and Location to separate data set.  
* [GPDD_Data.R](Code/GPDD_Data.R): Draws a world map and superimposes all coordinate points.  

