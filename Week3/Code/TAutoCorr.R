# An R script that calculate the correlation between n−1 pairs of years,
# where n is the total number of years. 

rm(list = ls()) #clean current obejcts in workspace
set.seed(1)#set random seed

ats <- get(load("../Data/KeyWestAnnualMeanTemperature.RData"))# load data

#create two vectors x_t0 and x_t1 such that they correspond to x[t]-x[t-1] pairs
#using cor() to calculate the correlation
#OR using acf()
#ac <- acf(ats$Temp,lag.max = 1, plot = F)
x_t0 <- head(ats$Temp, -1) #every element in ats$Temp except last one
x_t1 <- tail(ats$Temp, -1) #every element in ats$Temp except first one
ac.tag1 <- cor(x_t1, x_t0) # correlation coefficient between successive years