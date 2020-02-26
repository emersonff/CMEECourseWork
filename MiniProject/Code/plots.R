library("ggplot2")
library("dplyr")
rm(list = ls())
graphics.off()
d <- read.csv("../Data/NewData.csv", header = T)
 
 p <- ggplot(d, aes(x = Time, y = log10(PopBio), color = Temp))
 p <- p + geom_point(size =I(0.3))
 p <- p + facet_wrap(~Species, nrow = 5, ncol = 9, strip.position = "bottom")
length(table(d$Species)) #45
length(table(d$Temp)) #17

#save in pdf Temp
pdf("../Results/Temp.pdf")
p
graphics.off()


a <- d %>% group_by(Species, Citation) %>% summarise()#45

subsets <- apply(a, 1, function(x){
  subset(d, d$Species == x[1] & d$Citation == x[2])
})

pdf("../Results/plots.pdf")
plots <- lapply(subsets, function(x){
  p <- ggplot(x, aes(x = Time, y = log10(PopBio), color = Medium))
  p <- p + geom_point(size =I(0.3))
  p <- p + facet_wrap(~Temp, strip.position = "bottom")
  p <- p + ggtitle(x[1, 7])
  print(p)
})
graphics.off()

