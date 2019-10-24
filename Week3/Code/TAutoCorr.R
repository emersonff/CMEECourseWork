# An R script that calculate the correlation between n−1 pairs of years,
# where n is the total number of years. 

rm(list = ls()) #clean current obejcts in workspace
set.seed(1)#set random seed

ats <- get(load("../Data/KeyWestAnnualMeanTemperature.RData"))# load data

#create two vectors x_t0 and x_t1 such that they correspond to x[t]-x[t-1] pairs
#using cor() to calculate the correlation between 2 vectors
x_t0 <- head(ats$Temp, -1) #every element in ats$Temp except last one
x_t1 <- tail(ats$Temp, -1) #every element in ats$Temp except first one
ac.tag1 <- cor(x_t1, x_t0) # correlation coefficient between successive ac
print(paste("the appropriate correlation coefficient between successive years:", ac.tag1))

# permute time series using sample()
#repeat calculation 10000 times and save in a matrix
results <- matrix()
for (i in 1:10000){
  s1 <- sample(x = ats$Temp, size=99, replace=T)
  s2 <- sample(x = ats$Temp, size=99, replace=T)
  results[i] <- cor(s1, s2)
}
#print(results)

#calculate the fraction of results that is greater than correlation between successive years
approx_p <- sum(results > ac.tag1) / 10000
print(paste("approximate p-value:", approx_p))









