MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F,stringsAsFactors = F))
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T, sep = ";", stringsAsFactors = F)

MyData[MyData == ""] = 0
MyData <- t(MyData) 
#class(MyData)
#head(MyData)
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F)##data.frame that does not contain the first row of matrix
colnames(TempData) <-MyData[1,]
rownames(TempData) <-NULL
require(reshape2)
#print(head(TempData))
MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
MyWrangledData[,"Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])


MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
#str(MyWrangledData)

require(dplyr)

print(dplyr::tbl_df(MyWrangledData))# like head()
dplyr::glimpse(MyWrangledData)# like str()
utils::View(MyWrangledData) #same as fix()
dplyr::filter(MyWrangledData, Count > 100) #like subset(), but nicer!




