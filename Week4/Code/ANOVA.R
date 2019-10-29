d<- read.table("../Data/SparrowSize.txt",  header=TRUE) 	
d1<-subset(d,  d$Wing!="NA") 	


summary(d1$Wing) 	

hist(d1$Wing) 	
model1 <- lm(Wing~Sex.1, data = d1)
summary(model1)
boxplot(d1$Wing~d1$Sex.1,  ylab="Wing  length  (mm)") 	
anova(model1) 	

t.test(d1$Wing~d1$Sex.1,  var.equal=TRUE) 	
model2 <- lm(Wing~BirdID, data = d1)
anova(model2)
  summary(model2)
boxplot(d1$Wing~d1$BirdID,  ylab="Wing  length  (mm)") 	

require(dplyr) 	

tbl_df(d1)
glimpse(d1) 	


d$Mass  %>%  cor.test(d$Tarsus,  na.rm=TRUE) 	

d1  %>% group_by(BirdID)%>% summarise  (count=length(BirdID))  
count(d1,  BirdID) 	
d1  %>% group_by(BirdID)%>% summarise  (count=length(BirdID)) %>%count(count) 	

model3 <-lm(Wing~as.factor(BirdID), data=d1)
anova(model3)
boxplot(d$Mass~d$Year) 	


