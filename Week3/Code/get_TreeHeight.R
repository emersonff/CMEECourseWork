# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# a .csv file which includes follows:
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"
##############
#take a csv file name from the command line(e.g trees.csv)
#Loads the .csv file and calculates tree heights for all trees in the data. 
#Creates a csv output file named as InputFileName_treeheights.csv in results that contains the calculated 
#tree heights along with the original data 

rm(list = ls()) #clean current obejcts in workspace

###functions
TreeHeight <- function(m){ #m[,1]:species    m[,2]:distances in meter    m[,3]: degrees
#apply calculations on each column
  radians <- as.numeric(m[,3]) * pi /180 ##coerce from character to numeric type for calculation
  height <-as.numeric(m[,2]) * tan(radians)
  return (height) #return a vector of heights
}

##handling command line argument
args <- commandArgs(trailingOnly = T) 
if(length(args) == 0){
  stop("No input file.")
}

trees.df <- read.csv(args[1]) # read csv file
trees.m <- as.matrix(trees.df)#matrix using matrix instead of data.frame because it is faster when lager number of mathematical 
#calculations

trees.df$Tree.Height.m <-TreeHeight(trees.m)

#split argument using / and . to get input filename; using paste() to get output filename
filename <- paste("../Results/", strsplit(args[1], "/|\\.")[[1]][5], "_treeheights.csv", sep = "")

write.csv(file = filename, trees.df) #write results
print(paste("results are written into", filename))



