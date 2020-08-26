####R script to read all metadata from extracted csv file
### slower than python
rm(list = ls())#clear workspace
library(stringr)
d <- read.csv("../Data/data.csv", header = T, stringsAsFactors = F)#read raw csv file
n <- nrow(d)# 418745 objects in total 
head(d)
#remove redundant reletive paths to the source files
d$SourceFile <- str_extract(d$SourceFile, "\\d+_HH_.*")
d$Keywords <- str_replace(d$Keywords, "Human Presence", "Human Presence: 1")#for consistency
#tags <- strsplit(d$Keywords, ",\\s*|:\\s*")
#a <- lapply(tags, function(x){# a nested list
#  strsplit(x, ":\\s*")
#})


##extract all tags
#[1] "placeID"        "species1"       "Human Presence" "contact1"       "contact2"      
#[6] "species2"       "species3"       "contact3"       "Site"           "Sp"            
#[11] "n"              "good photo"
#rep("good photo", d$Keywords, value = T)
#[1] "good photo, placeID: 08, species1: Hedgehog"
# delete tag good photo since it is irrelevant and has only 1 instance
t <- proc.time()
tags <- strsplit(d$Keywords, ",\\s*")
tags.uni <- unique(str_replace(unlist(tags), ":.*", ""))[-12]
tags.d <- sapply(tags.uni, function(x){
      x <- sapply(tags, function(y){
        #temp <- str_match(unlist(y), paste0(x,":\\s(.*)"))[,2]
        #temp[!is.na(temp)]
        na.omit(str_match(unlist(y), paste0(x,":\\s(.*)"))[,2])[1]
      })
})
#tags.d[tags.d == character(0)] <- NA
tags.d <- as.data.frame(tags.d)
t <- proc.time() - t





