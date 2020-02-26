library("ggplot2")
rm(list = ls())#clear workspace
graphics.off()

#read data
load("../Data/Fittings.RData")#loading fitting results
load("../Data/Predicts.RData")
d <- read.csv("../Data/NewData.csv", header = T)
#Filter(Negate(anyNA), Fit.Buchanan)remove NAs

pdf("../Results/final_plots.pdf")
lapply(seq(length(unique(d$ID))), function(x){
  id <- unique(d$ID)[x]
  subd <- d[d$ID == id, ]
  title <- paste(unlist(strsplit(as.character(id),"_"))[-4], collapse = "_")
  p <- ggplot(subd, aes(x = Time, y = lnN)) + geom_point(size = 3) +
    geom_line(data = predict.all[[x]], aes(x = Time, y = Predict, col = Model), size = 1) +
    theme_bw(base_size = 16) +
    theme(aspect.ratio = 1) +
    labs(x = "Time", y = "lnN") + ggtitle(paste(x, title, sep = ": "))
  #p
})
graphics.off()