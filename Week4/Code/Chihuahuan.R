rm(list = ls())
library(ggplot2)
a <- read.csv("../Data/rodents.csv")
a <- subset(a, sex == "M" | sex == "F", rm.na = T)
require(lme4)
lmm <- lm(hfl~ precip + species, data = a)
summary(lmm)

lmm2 <- lmer(hfl~ precip + (1|species), data = a)
summary(lmm2)

require(dplyr) 	

p <- ggplot(a, aes(x = precip, y = hfl))
#p <- p+ geom_boxplot()
p <- p + geom_point(size=I(.3))
p <- p +geom_smooth(method = "lm", fullrange=TRUE,alpha=I(.3), size = I(0.5))
p <- p + facet_wrap(~species,  ncol=4,nrow=7, strip.position = "right") 
p <- p +ylim(0, 65)
png("../Results/hfl_precip.png")
p
graphics.off()