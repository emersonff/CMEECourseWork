rm(list = ls())
library(ggplot2)
library(plyr)
MyDF = read.csv("../Data/EcolArchives-E089-51-D1.csv")#read data

##plotting using ggplot()
p <- ggplot(MyDF, aes(x = Prey.mass, y = Predator.mass,
                      color = Predator.lifestage))
p <- p + geom_point(alpha=I(.5), shape=I(3)) + geom_smooth(method = "lm", fullrange=TRUE) #add points and regression lines
p <- p + theme_bw() + theme(legend.position = "bottom")#set theme
p <- p + labs(x = "Prey mass in grams", y = "Predator mass in grams" )
p <- p + facet_wrap(~Type.of.feeding.interaction,  ncol=1, strip.position = "right") ##add facets
p <- p + scale_x_continuous(trans = 'log10') + scale_y_continuous(trans = 'log10') #using log scale

#save in pdf
pdf("../Results/PP_Regress.pdf")
p
graphics.off()

#calculate the regression results
results <- ddply(MyDF, .(Type.of.feeding.interaction, Predator.lifestage), function(x){
  model <- lm(log10(x$Predator.mass) ~ log10(x$Prey.mass)) #model y~x
  slope <- summary(model)$coefficient[2] #estimate slope
  intercept <- summary(model)$coefficient[1] #estimate intercept
  R2 <- summary(model)$r.squared
  f <- summary(model)$fstatistic[1]# have NUll in it so row numbers are different
  f[is.null(f)] <- 0 ##remove NULL 
  p <- summary(model)$coefficient[1,4]
  data.frame(slope = slope, intercept = intercept, R2 = R2, F_statistic = f, p_value = p)

} )

write.csv(results, "../Results/PP_Regress_Results.csv")

