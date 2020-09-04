####Calculate summary statistics and do plots
library("ggplot2")
library("dplyr")
library("stringr")
library("overlap")
rm(list = ls())#clear workspace
#graphics.off()

d <- read.csv("../Results/results_d.csv", header = T, stringsAsFactors = F)
t_d <- read.csv("../Results/cm_re.csv", header = T, stringsAsFactors = F)
### convert time to radian time
ToRadian<- function(string){
  seconds <- as.numeric(substr(string, 12,13)) * 3600 + as.numeric(substr(string, 15,16)) * 60 + as.numeric(substr(string, 18,19))
  radian <- seconds * (pi / 64800) # scale from 0 to 1
  return(radian)
}

d$radian_time <- sapply(d$CreateDate, ToRadian)
t_d$radian_time <- sapply(t_d$CreateDate, ToRadian)
#####density fit for openpose results
sub_op_d <- subset(d, OpenPose == 1)
densityPlot(sub_op_d$radian_time)

####density fit for classifier results
sub_cl_d <- subset(d, IsHuman == 1)
densityPlot(sub_cl_d$radian_time)

#####using activity package
library(activity)

####density of misclassification on test data.
t_opmod <- fitact(sub_op_d$radian_time)
sub_op_td <- t_d[which(t_d$actual != t_d$OpenPose),]
sub_cl_td <- t_d[which(t_d$actual != t_d$Classifer),]
t_opmod <- fitact(sub_op_td$radian_time)
t_clmod <- fitact(sub_cl_td$radian_time)
plot(t_opmod, yunit="density", data="histogram")
plot(t_clmod, yunit="density", data="histogram", add=TRUE, tline=list(col="red"))
legend("topright", c("OpenPose", "Classifier"), col=1:2, lty=1)



###### density of human images for both openpose and classifer
opmod <- fitact(sub_op_d$radian_time)
clmod <- fitact(sub_cl_d$radian_time)
png("../Results/time_den_all.png")
plot(opmod, yunit="density", data="none")
plot(clmod, yunit="density", data="none", add=TRUE, tline=list(col="red"))
legend("topright", c("OpenPose", "Classifier"), col=1:2, lty=1)
graphics.off()
compareCkern(opmod, clmod, reps = 50)
######density of misclassification (having different classification results) 
a <- sub_cl_d$SourceFile
b <- sub_op_d$SourceFile
#dif <- setdiff(union(a,b), intersect(a,b))
da <- sub_cl_d[which(a %in% setdiff(a, b)),]# images with misclassification
db <- sub_op_d[which(b %in% setdiff(b, a)),]# images with misclassification
diff <-rbind(da,db)# images with misclassification
diffmod <- fitact(diff$radian_time)
#png("../Results/Ske_TimeDist.png")
plot(diffmod, yunit="density", data="histogram")


#######density of fullly skeletons

### distribution of human images classified using openpose
op_hu <- subset(d, d$OpenPose == 1)
p1<-ggplot(data = op_hu, aes(x = placeID)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("place ID") + ylab("count") + 
  #ggtitle("Site distribution of pictures classified \n as human \n images using BODY-25 model")+
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1


