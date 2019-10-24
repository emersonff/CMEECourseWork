#Script that draws and saves three lattice graphs by feeding interaction type: 
#one of predator mass, one of prey mass and one of the size ratio of prey mass over predator mass.
#In addition, the script will calculate the mean and median predator mass, 
#prey mass and predator-prey size-ratios to a csv file.
rm(list=ls())
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
#create data frame to store results
#results <- data.frame(matrix(ncol = 7, nrow = 5))
#names(results) <- c( "Feeding type","Pred_mean", "Pred_median", "Prey_mean", "Prey_median", "Ratio_mean", "Ratio_median")

#require(dplyr)
#dplyr::glimpse(MyDF)
library(lattice)
pdf("../Results/Pred_Lattice.pdf", 11.7, 8.3)#open blank pdf page
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off() # alternatively using dev.off()
pdf("../Results/Prey_Lattice.pdf", 11.7, 8.3)
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off()
pdf("../Results/SizeRatio_Lattice.pdf", 11.7, 8.3)
densityplot(~log(Prey.mass / Predator.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off()# alternatively using dev.off()

#subsets for calculating means and medians for different feeding types 
#sub.preda <- subset(MyDF, Type.of.feeding.interaction == "predacious")
#sub.pp <- subset(MyDF, Type.of.feeding.interaction == "predacious/piscivorous")
#sub.insec <- subset(MyDF, Type.of.feeding.interaction == "insectivorous")
#sub.pisci <- subset(MyDF, Type.of.feeding.interaction == "piscivorous")
#sub.plank <- subset(MyDF, Type.of.feeding.interaction == "planktivorous")

require(plyr)
results <- ddply(MyDF,"Type.of.feeding.interaction", function(x){
  Pred_mean <- mean(log(x$Predator.mass))
  Pred_median <- median(log(x$Predator.mass))
  Prey_mean <- mean(log(x$Prey.mass))
  Prey_median <- median(log(x$Prey.mass))
  Ratio_mean <- mean(log(x$Prey.mass / x$Predator.mass))
  Ratio_median <- median(log(x$Prey.mass / x$Predator.mass))
  data.frame(Pred_mean = Pred_mean, Pred_median = Pred_median, Prey_mean
             = Prey_mean, Prey_median = Prey_median , Ratio_mean = Ratio_mean, Ratio_median = Ratio_median)
} )

write.csv(results, "../Results/PP_Results.csv")





