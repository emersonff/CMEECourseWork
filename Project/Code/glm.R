####Calculate summary statistics and do plots
library("ggplot2")
library("dplyr")
library("stringr")
rm(list = ls())#clear workspace
graphics.off()

#read csv files
json_d <- read.csv("../Data/SkeletonCount.csv", header = T, stringsAsFactors = F)
final_d <- read.csv("../Data/Final_Data.csv", header = T, stringsAsFactors = F)
#json_d$h <- substr(json_d$CreateDate, 12, 13)#extract hours


#check the maximum number of human detected in a single image and that image file name.
max(json_d$Count)#maximum number of human detected in a single image : 11
json_d$SourceFile[which(json_d$Count == max(json_d$Count))]#"23_HH_23_4_18_DCIM/100_BTCF/IMG_1601.JPG" 

#
length(unique(final_d$placeID))#136: number of sites in total
length(unique(json_d$placeID))# 133: number of sites which contian full skeleton data
table(json_d$Count)# counts of images having different number of full skeleton data

png("../Results/Ske_CountDist.png")
p1<-ggplot(data = json_d, aes(x = Count)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("number of skeletons per image") + ylab("count") + 
  ggtitle("Distribution of images having different\n number of skeletons") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()

png("../Results/Ske_TimeDist.png")
temp <- json_d %>% group_by(h) %>% summarise(Count=sum(Count))
p1<-ggplot(data = temp, aes(x = h, y = Count)) +
  geom_bar(stat="identity") + theme_bw(base_size = 16) +
  xlab("hours") + ylab("count") + 
  ggtitle("Time distribution of skeletons") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()