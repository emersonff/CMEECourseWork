################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

############# Load the dataset ###############
require(tidyr)
require(dplyr)

# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <-dplyr::tbl_df(read.csv("../Data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F))

############# Inspect the dataset ###############
dplyr::tbl_df(MyData)
dim(MyData)
dplyr::glimpse(MyData)#str(MyData)
#fix(MyData) #you can also do this # a form
View(MyData)#View data set in spreadsheet-like display
#fix(MyMetaData)
View(MyMetaData)



############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData) 
dplyr::tbl_df(MyData)
dim(MyData)

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############
## not to gather Cultivation", Block, Plot and Quadrat
MyWrangledData <- tidyr::gather(TempData, key = "Species", value = "Count", -Cultivation, -Block, -Plot, -Quadrat)
#MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])

#str(MyWrangledData)
dplyr::glimpse(MyWrangledData) #like str(), but nicer!
dplyr::tbl_df(MyWrangledData) #like head(), but nicer!
dim(MyWrangledData)

############# Exploring the data (extend the script below)  ###############


dplyr::glimpse(MyWrangledData) #like str(), but nicer!
dplyr::filter(MyWrangledData, Count > 100) #like subset(), but nicer!
dplyr::slice(MyWrangledData, 10:15) # Look at an arbitrary set of data rows
