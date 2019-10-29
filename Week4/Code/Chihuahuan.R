rm(list = ls())
library(ggplot2)
a <- read.csv("../Data/rodents.csv")
#a <- subset(a, a$sex != P)
model <- lm(hfl~precip+species, data = a)
#boxplot(hfl~precip+tag, data = a)

require(dplyr) 	

p <- ggplot(a, aes(x = precip, y = hfl,
                      color = sex))
#p <- p+ geom_boxplot()
p <- p +geom_smooth(method = "lm", fullrange=TRUE,alpha=I(.3), size = I(0.5))
p <- p + facet_wrap(~species,  ncol=4,nrow=7, strip.position = "right") 
pdf("../Results/hfl_precip.pdf")
p
graphics.off()