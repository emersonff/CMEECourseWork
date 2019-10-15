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

###functions
TreeHeight <- function(data){ #data[1]:species    data[2]:distances in meter    data[3]: degrees
  for(i in data){}
  radians <- degrees * pi /180
  height <-distance * tan(radians)
  print(paste("The tree heightis:", height))
  
  return (height)
}



datax <- read.csv("../Data/trees.csv")
TreeHeight(37, 40)




