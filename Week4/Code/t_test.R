rm(list=ls()) 	

d <- read.table("../Data/SparrowSize.txt", header = TRUE)#read data

boxplot(d$Mass ~ d$Sex.1, col = c("red", "blue"), ylab = "body mass(g)")

t.test1 <- t.test(d$Mass ~ d$Sex.1)
print(t.test1)

d1 <- as.data.frame(head(d,50))#first 50 rows of data

t.test2 <- t.test(d1$Mass ~ d1$Sex.1)
print(t.test2)

d2001 <- subset(d,d$Year == 2001)
t.wing.2001 <- t.test(d2001$Wing)
t.wing <- t.test(d$Wing)
print(t.wing.2001)

t.wing.2001.mf <- t.test(d2001$Wing ~ d2001$Sex.1)
t.wing.mf <- t.test(d$Wing ~ d$Sex.1)
require(pwr)
print(pwr.t.test(d=0.5/sd(d$Wing, na.rm=T), power=0.8, sig.level = .05, type = "two.sample", alternative = "two.sided"))
# d:effect size  sig.level: Type1 error prob        power:1-type2 error pro







