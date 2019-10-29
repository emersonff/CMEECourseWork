rm(list=ls())
d <- read.table("../Data/SparrowSize.txt", header = TRUE)#read data

str(d)
hist(d$Tarsus)
print(mean(d$Tarsus, na.rm = T))
print(median(d$Tarsus, na.rm = T))
print(mode(d$Tarsus))

par(mfrow =  c(2, 2)) ##mfrow is a vector of the form c(nr,nc) layout of subsequent figures
hist(d$Tarsus, breaks = 3, col = "grey")
hist(d$Tarsus, breaks = 10, col = "grey")
hist(d$Tarsus, breaks = 30, col = "grey")
hist(d$Tarsus, breaks = 100, col = "grey")

par(mfrow = c(2,2))
Bill.mean <- mean(d$Bill, na.rm =T)
Wing.mean <- mean(d$Wing, na.rm =T)
Mass.mean <- mean(d$Mass, na.rm = T)
Bill.var <- var(d$Bill, na.rm = T)
Wing.var <- var(d$Wing, na.rm = T)
Mass.var <- var(d$Mass, na.rm = T)
Bill.sd <- sd(d$Bill, na.rm = T)
Wing.sd <- sd(d$Wing, na.rm = T)
Mass.sd <- sd(d$Mass, na.rm = T)

par(mfrow =  c(2, 2)) ##mfrow is a vector of the form c(nr,nc) layout of subsequent figures
hist(d$Tarsus, col = "grey")
hist(d$Bill, breaks = 10, col = "grey")
hist(d$Wing, col = "grey")
hist(d$Mass, col = "grey")


