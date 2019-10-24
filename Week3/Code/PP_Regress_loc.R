rm(list = ls())
library(ggplot2)
library(plyr)
MyDF = read.csv("../Data/EcolArchives-E089-51-D1.csv")#read data

##calculate the regression results
results <- ddply(MyDF, .(Type.of.feeding.interaction, Predator.lifestage, Location), function(x){
  model <- lm(log10(x$Predator.mass) ~ log10(x$Prey.mass)) #model y~x
  slope <- summary(model)$coefficient[2] #estimate slope
  intercept <- summary(model)$coefficient[1] #estimate intercept
  R2 <- summary(model)$r.squared
  f <- summary(model)$fstatistic[1]# have NUll in it so row numbers are different
  f[is.null(f)] <- 0 ##remove NULL 
  p <- summary(model)$coefficient[1,4]
  data.frame(slope = slope, intercept = intercept, R2 = R2, F_statistic = f, p_value = p)
  
} )

write.csv(results, "../Results/PP_Regress_loc_Results.csv")
