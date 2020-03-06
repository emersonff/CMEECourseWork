#Author: Xiang Li(xiang.li419@imperial.ac.uk)
library("ggplot2")
rm(list = ls())#clear workspace
graphics.off()

#read data
load("../Results/Fittings.RData")#loading fitting results
load("../Results/Predicts.RData")
d <- read.csv("../Results/NewData.csv", header = T)
RSS <- read.csv("../Results/RSS.csv", header = T)
AIC <- read.csv("../Results/AIC.csv", header = T)
AICc <- read.csv("../Results/AICc.csv", header = T)
BIC <- read.csv("../Results/BIC.csv", header = T)
abbr <- c("A","B", "Bb", "b", "G", "GB", "L", "LB", "LG", "LGB", "LGBb")# abbrivation for model names
temp <- data.frame(ID = seq(length(dID)),Length = n )

### plotting number of successful fits of each model
temd <- data.frame(Model = c("Logistic", "Gompertz", "Baranyi", "Buchanan"),
      Fits = c(length(fit.Logistic[!is.na(fit.Logistic)]),length(fit.ModifiedGompertz[!is.na(fit.ModifiedGompertz)]),
      length(fit.Baranyi[!is.na(fit.Baranyi)]), length(fit.Buchanan[!is.na(fit.Buchanan)])))
pdf("../Results/Number_Fits.pdf")
p<-ggplot(data = temd, aes(x = Model, y = Fits)) +
  geom_bar(stat ="identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

### plotting number of best fits according the RSS
pdf("../Results/Best_RSS.pdf")
temp <- data.frame(Model = levels(unique(RSS$Best.model)), Number = as.vector(table(RSS$Best.model)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

#temp.RSS <- data.frame(Model = levels(unique(RSS$Best.model)), Number = as.vector(table(RSS$Best.model)), Method = "RSS")
#temp.AIC <- data.frame(Model = levels(unique(AIC$Smallest.AIC)), Number = as.vector(table(AIC$Smallest.AIC)), Method = "AIC")
#temp.BIC <- data.frame(Model = levels(unique(BIC$Smallest.BIC)), Number = as.vector(table(BIC$Smallest.BIC)), Method = "BIC")
#temp.AICc <- data.frame(Model = levels(unique(AICc$Smallest.AICc)), Number = as.vector(table(AICc$Smallest.AICc)), Method = "AICc")
#temp <- rbind(temp.RSS,temp.AIC, temp.BIC, temp.AICc)
#p<-ggplot(data = temp, aes(x = Model, y = Number, group = Method)) +
#  geom_bar(data = temp, stat = "identity") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
#p

# plotting number of best fits according the AIC
pdf("../Results/Smallest_AIC.pdf")
temp <- data.frame(Model = levels(unique(AIC$Smallest.AIC)), Number = as.vector(table(AIC$Smallest.AIC)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

pdf("../Results/Best_AIC.pdf")
temp <- data.frame(Model = abbr, Number = as.vector(table(AIC$Best.model)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

# plotting number of best fits according the AIC
pdf("../Results/Smallest_BIC.pdf")
temp <- data.frame(Model = levels(unique(BIC$Smallest.BIC)), Number = as.vector(table(BIC$Smallest.BIC)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

pdf("../Results/Best_BIC.pdf")
temp <- data.frame(Model = abbr, Number = as.vector(table(BIC$Best.model)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

# plotting number of best fits according the AICc
pdf("../Results/Smallest_AICc.pdf")
temp <- data.frame(Model = levels(unique(AICc$Smallest.AICc)), Number = as.vector(table(AICc$Smallest.AICc)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

pdf("../Results/Best_AICc.pdf")
temp <- data.frame(Model = abbr, Number = as.vector(table(AICc$Best.model)))
p<-ggplot(data = temp, aes(x = Model, y = Number)) +
  geom_bar(stat = "identity", color = "lightgray") + theme_bw(base_size = 16) + theme(aspect.ratio = 1)
p
graphics.off()

### plotting predicted points for each model of each data set
pdf("../Results/final_plots.pdf")
lapply(seq(length(unique(d$ID))), function(x){
  id <- unique(d$ID)[x]
  subd <- d[d$ID == id, ]
  title <- paste(unlist(strsplit(as.character(id),"_"))[-4], collapse = "_")
  p <- ggplot(subd, aes(x = Time, y = lnN)) + geom_point(size = 3) +
    geom_line(data = predict.all[[x]], aes(x = Time, y = Predict, col = Model), size = 0.5) +
    theme_bw(base_size = 16) +
    theme(aspect.ratio = 1) +
    labs(x = "Time", y = "lnN") + ggtitle(x)
  #p
})
graphics.off()