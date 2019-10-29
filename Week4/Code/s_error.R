rm(list=ls()) 	

d <- read.table("../Data/SparrowSize.txt", header = TRUE)#read data

d1<- subset(d,  d$Tarsus!="NA") 	

seTarsus<- sqrt(var(d1$Tarsus)/length(d1$Tarsus)) 	

print(seTarsus)


d12001 <- subset(d1, d1$Year == 2001)
seTarsus2001 <- sqrt(var(d12001$Tarsus)/length(d12001$Tarsus))
print(seTarsus2001)

# mass
dm <- subset(d, d$Mass != "NA")
dw <- subset(d, d$Wing != "NA")
db <- subset(d, d$Bill != "NA")
dm2001 <- subset(dm, dm$Year == 2001)
dw2001 <- subset(dw, dw$Year == 2001)
db2001 <- subset(db, db$Year == 2001)
seMass <- sqrt(var(dm$Mass)/length(dm$Mass))##standard error of Mass, Wing and Bill
seWing <- sqrt(var(dw$Wing)/length(dw$Wing))
seBill <- sqrt(var(db$Bill)/length(db$Bill))

seMass2001 <- sqrt(var(dm2001$Mass)/length(dm2001$Mass))#stand error of Mass, Wing and Bill in 2001
seWing2001 <- sqrt(var(dw2001$Wing)/length(dw2001$Wing))
seBill2001 <- sqrt(var(db2001$Bill)/length(db2001$Bill))

###confidence interval is ci = [mean-1.96sd, mean+1.96sd]
#t.test(d1$Tarsus,mu=18.5,na.rm=TRUE)

