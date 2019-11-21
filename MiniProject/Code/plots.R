library("ggplot2")
library("dplyr")
d <- read.csv("../Data/LogisticGrowthData.csv", header = T)
dimmd <- read.csv(("../Data/LogisticGrowthMetaData.csv"),header = T)#meta data

d <- subset(d, d$Time >= 0 & d$PopBio >0)
 
 p <- ggplot(d, aes(x = log10(Time), y = log10(PopBio), color = Temp))
 p <- p + geom_point(size =I(0.3))
 p <- p + facet_wrap(~Species, nrow = 5, ncol = 9, strip.position = "bottom")
length(table(d$Species)) #45
length(table(d$Temp)) #17

#save in pdf Temp
pdf("../Results/Temp.pdf")
p
graphics.off()


p <- ggplot(d, aes(x = log10(Time), y = log10(PopBio), color = Medium))
p <- p + geom_point(size =I(0.3))
p <- p + facet_wrap(~Species, nrow = 5, ncol = 9, strip.position = "bottom")
pdf("../Results/Medium.pdf")
p
graphics.off()

p <- ggplot(d, aes(x = log10(Time), y = log10(PopBio)))
p <- p + geom_point(size =I(0.3))
#p <- p + facet_wrap(~Species, nrow = 5, ncol = 9, strip.position = "bottom")
pdf("../Results/overall_pops.pdf")
p
graphics.off()


#p <- ggplot(d, aes(x = Species, y = PopBio))
#p <- p + geom_boxplot()
#p <- p + facet_wrap(~Temp, nrow = 5, ncol = 4, strip.position = "bottom")

a <- d %>% group_by(Species, Citation) %>% summarise()

subsets <- apply(a, 1, function(x){
  subset(d, d$Species == x[1] & d$Citation == x[2])
})

pdf("../Results/plots.pdf")
for(i in 1:length(subsets)){
  p <- ggplot(subsets[[i]], aes(x = Time, y = log10(PopBio), color = Medium))
  p <- p + geom_point(size =I(0.3))
  p <- p + facet_wrap(~Temp, strip.position = "bottom")
  print(p)
}
graphics.off()

