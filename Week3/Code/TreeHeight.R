# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"
##############
#Loads trees.csv and calculates tree heights for all trees in the data. 
#Note that the distances have been measured in meters. (Hint: use relative paths)).
#
#Creates a csv output file called TreeHts.csv in results that contains the calculated 
#tree heights along with the original data 


rm(list = ls()) #clean current obejcts in workspace
###functions
TreeHeight <- function(m){ #m[,1]:species    m[,2]:distances in meter    m[,3]: degrees
  #apply calculations on each column
  radians <- as.numeric(m[, 3]) * pi /180 ##coerce from character to numeric type for calculation
  height <-as.numeric(m[, 2]) * tan(radians)
  return (height) #return a vector of heights
}



trees.df <- read.csv("../Data/trees.csv") # data.frame
trees.m <- as.matrix(trees.df)#matrix using matrix instead of data.frame because it is faster when lager number of mathematical 
                              #calculations

trees.df$Tree.Height.m <- TreeHeight(trees.m)
write.csv(file = "../Results/TreeHts.csv", trees.df) #write results
print("results has been written.")



