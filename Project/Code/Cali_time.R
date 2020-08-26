####Calculate summary statistics and do plots
library("ggplot2")
library("dplyr")
library("stringr")
rm(list = ls())#clear workspace
graphics.off()

d <- read.csv("../Results/results_d.csv", header = T, stringsAsFactors = F)
td <- read.csv("../Results/test_d_2.csv", header = T, stringsAsFactors = F)
#check h = 0,1,2,3,4,5 means morning or afternoon
#dif_d <- subset(d, abs(IsHuman - OpenPose) != 0)
#dif_td <- subset(td, actual - OpenPose == 1)

#for sample images
dif_td <- subset(td, abs(actual - OpenPose) == 1)
png("../Results/misclassified_time_test.png")
p2<-ggplot(data = dif_td, aes(x = h)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("time") + ylab("count") + 
  ggtitle("count of incorretly classified images \n at each time period") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p2
graphics.off()


dif_c <- dif_td %>% group_by(h) %>% count()#count for images of which the classified results are different
total_c <- td %>% group_by(h) %>% count()#to

require(lme4)

####for all images
dif_d <- subset(d, abs(IsHuman - OpenPose) == 1)#false negative
nrow(dif_d)
png("../Results/misclassified_time_all.png")
p1<-ggplot(data = dif_d, aes(x = h)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("time") + ylab("count") + 
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()
dif_c <- dif_d %>% group_by(h) %>% count()#count for images of which the classified results are different
total_c <- d %>% group_by(h) %>% count()#totoal count of images at different time period
dif_c$p <- dif_c$n / total_c$n
#mean(dif_c$n) 3428.292
#sd(dif_c$n) 3134.374

total_d_lmm <- dif_d %>% group_by(placeID, h)  %>% count()# using in lmmd
colnames(total_d_lmm) <- c("placeID", "time", "count")
total_d_lmm$placeID <- as.factor(total_d_lmm$placeID)
total_d_lmm$time <- as.factor(total_d_lmm$time)
lmm<-lmer(count~ time + (1 | placeID),data = total_d_lmm)
summary(lmm)

#percentage of misclassified image for all images explained in time and site
d$abs <- abs(d$IsHuman - d$OpenPose)
total_diff <- d %>% group_by(placeID, h)  %>% summarise(count_diff = sum(abs))
total_c <- d %>% group_by(placeID, h) %>% count()
total_diff$percent <- total_diff$count_diff / total_c$n
colnames(total_diff) <- c("placeID", "time", "count", "percentage")
total_diff$placeID <- as.factor(total_diff$placeID)
total_diff$time <- as.factor(total_diff$time)
lmm<-lmer(percentage~ time + (1 | placeID),data = total_diff)
summary(lmm)


#misclassified rates at different time
h_diff <- d %>% group_by(h)  %>% summarise(count_diff = sum(abs))
h_c <- d %>% group_by(h) %>% count()
h_diff$percent <- h_diff$count_diff / h_c$n
ggplot(h_diff, aes(x=h, y=percent)) + geom_point()

png("../Results/misclassified_rate_time_all.png")
p1<-ggplot(data = h_diff, aes(x=h, y=percent)) +
  geom_point() + theme_bw(base_size = 16) +
  xlab("time") + ylab("misclassified rate") + 
  ggtitle("misclassified rates against time") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()

png("../Results/misclassified_rate_time_all_boxplot.png")
p1<-ggplot(data = total_diff, aes(x=time, y=percentage)) +
  geom_boxplot() + theme_bw(base_size = 16) +
  xlab("time") + ylab("misclassified rate") + 
  ggtitle("misclassified rates against time") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()


lmm<-lmer(percentage~ time + (1 | placeID),data = total_diff)
summary(lmm)

lmm<-lmer(percentage~ placeID + (1 | time),data = total_diff)
summary(lmm)

lmm<-lm(percentage~ placeID +  time,data = total_diff)
summary(lmm)

