####Calculate summary statistics and do plots
library("ggplot2")
library("dplyr")
library("stringr")
rm(list = ls())#clear workspace
graphics.off()
d <- read.csv("../Results/New_Merged_Data.csv", header = T, stringsAsFactors = F)#read raw csv file
#d$h <- substr(d$CreateDate, 12, 13)#extract hours
d$placeID <- coalesce(d$placeID, d$Site)
d$placeID <- coalesce(d$placeID, d$ID)
d$Site <- NULL
d$species1 <- coalesce(d$species1, d$sp)
d.tags<- subset(d, d$Keywords != "")



###### pictures with no tags ######
d.noTags <- subset(d, d$Keywords=="")
nrow(d.noTags) # 107528
nrow(d.noTags)/nrow(d)#0.25678
noTags_freq <- sapply(unique(d.noTags$Folder), function(x){#freq of pictures with no tags in each folder
  as.vector(table(d.noTags$Folder)[x] / table(d$Folder)[x])
  
})
noTags_freq <- as.table(noTags_freq)
#temp dataframe for plotting
temp1 <- as.data.frame(table(d.noTags$Folder))
temp2 <- as.data.frame(noTags_freq)
colnames(temp1) <- c("folder", "value")
colnames(temp2) <- c("folder", "value")
temp1$type <-"count"
temp2$type <-"percentage"
pd <- rbind(temp1, temp2)

png("../Results/NoTags_FolderDist.png")
p1<-ggplot(data = pd, aes(x = folder, y = value)) +
  geom_bar(stat="identity", color = "lightgray") + theme_bw(base_size = 16) +
  facet_wrap(~type,  ncol=2, strip.position = "top", scales = "free_x") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
  ggtitle("Folder distribution of unlabeled pictures") +
  coord_flip()
p1
graphics.off()


###### PlaceID, Human ######
temp1 <- as.data.frame(table(d.tags$placeID))
colnames(temp1) <- c("placeID", "count")
temp1$type <- "All pictures"
temp2 <- as.data.frame(table(d.tags$placeID[which(!is.na(d.tags$Human.Presence))]))
colnames(temp2) <- c("placeID", "count")
temp2$type <- "Pictures labeled with human presence"
pd <- rbind(temp1, temp2)

png("../Results/Ppl_SiteDist.png")
#p1<-ggplot(data = pd, aes(x = placeID, y = count, fill = type)) +
#  geom_bar(stat="identity", position=position_dodge()) + theme_bw(base_size = 16) +
#  scale_x_discrete(breaks=c(1, 30,60, 90, 120, 150)) +
#  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
#p1
p1<-ggplot(data = pd, aes(x = placeID, y = count)) +
  geom_bar(stat="identity") + theme_bw(base_size = 16) +
  facet_wrap(~type,  ncol=1, strip.position = "top", scales = "free_y") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) +
  ggtitle("Site distribution of labeled pictures") +
  scale_x_discrete(breaks=c(1, 30, 60, 90, 120, 150))
p1

graphics.off()

###### Time, Human  ###### time distribution of human image
pd <- subset(d.tags, !is.na(d.tags$Human.Presence))
png("../Results/Ppl_TimeDist.png")
p1<-ggplot(data = pd, aes(x = h, y = Human.Presence)) +
  geom_bar(stat="identity") + theme_bw(base_size = 16) +
  xlab("hours") + ylab("count of human images") + 
  ggtitle("Time distribution of images labeled \n with human presence") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()



###### Encounter  ######
#a <- c(d.tags$species1, d.tags$species2, d.tags$species3)
#unique(a)# 20 type of species labels in total
ah <- paste0(pd$species1, pd$species2, pd$species3)
ah <- str_replace_all(ah, "NA", "")
ah[ah == ""] <- NA
pd$species1 <- ah
pd$placeID <- as.factor(pd$placeID)
temp <- pd
temp$species1[which(!is.na(temp$species1))] <- "human and animal(s)"
temp$species1[which(is.na(temp$species1))] <- "only human"
png("../Results/Ppl_Ani_SiteDist2.png")
p1<-ggplot(data = temp, aes(x = placeID, fill = species1)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("place ID") + ylab("count") + 
  ggtitle("Site distribution of pictures labeled with human\n presence") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())+
  scale_x_discrete(breaks=c(1, 30, 60, 90, 120, 150))
p1
graphics.off()




pd <- pd[which(!is.na(pd$species1)),]
png("../Results/Ppl_Ani_SiteDist.png")
p1<-ggplot(data = pd, aes(x = placeID)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("place ID") + ylab("count") + 
  ggtitle("Site distribution of pictures labeled with human\n presence and species") +
  facet_wrap(~species1,  ncol=2, strip.position = "top", scales = "free") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()

png("../Results/Ppl_TotalAni_SiteDist.png")
p1<-ggplot(data = pd, aes(x = placeID)) +
  geom_bar() + theme_bw(base_size = 16) +
  xlab("place ID") + ylab("count") + 
  ggtitle("Site distribution of pictures labeled with human\n presence and species") +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
p1
graphics.off()

d$ID <- NULL
write.csv(d, "../Results/Final_Data.csv", row.names = F)

