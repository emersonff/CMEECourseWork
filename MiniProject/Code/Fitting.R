#Author: Xiang Li(xiang.li419@imperial.ac.uk)
library(minpack.lm)
library(dplyr)
library(nlstools)# using nlstools::confint2 to calculate confidence intervals
library(MuMIn) # calculate AICc
rm(list = ls())#clear workspace

#read data
d <- read.csv("../Results/NewData.csv", header = T)
dID <- unique(d$ID)
Models <- c("Logistic", "Gompertz", "Baranyi", "Buchanan")# used to selected best models
#######
#function object for the logistic model
Model.Logistic <- function(t, n0, nMax, r, tLag){# N0:initial population size, r: maximum growth rate, K: carrying capacity
  a <- nMax - n0
  return(n0 + a / (1 + exp(4 * r * (tLag - t) / a + 2)))
}

Model.ModifiedGompertz <- function(t, n0, nMax, r, tLag){# a:relative asymptote, tLag: duration of delay before growing exponentially
   a <- nMax - n0
   return(n0 + a * exp(-exp(r * exp(1) * (tLag - t) / a + 1)))
  
}

Model.Buchanan <- function(t, n0, r, tLag, tMax){#tMax: the time at which nMax is reached
  return((t <= tLag) * n0 + (t >= tMax) * (n0 + r * (tMax - tLag)) +
           (t > tLag & t < tMax) * (n0 + r * (t - tLag)))
}

Model.Baranyi <- function(t, n0, nMax, r, tLag){
  h0 <- tLag * r
 # at <- (1 / r) * log(exp(- r * t) + exp(-h0) - exp(- r * t - h0))
 # return(n0 + r * t + at - log(1 + (exp(r * t + at) - 1) / (exp(nMax - n0))))
  at <- t + log(exp(-r * t) + exp(-h0) - exp(-r * t - h0)) / r
  return(n0 + r * at - log(1 + (exp(r * at) - 1) / exp(nMax - n0)))

  
}


par <- sapply(dID, function(x){# calculating starting values of all the parameters
  subd <- data.frame(Time = d[d$ID == x, ]$Time, PopBio = d[d$ID == x, ]$PopBio,
                     lnN = d[d$ID == x, ]$lnN)#subset according to ID.
  ln.n0 <- subd$lnN[1]
  ln.nMax <- max(subd$lnN)
  ln.tMax <- subd$Time[which.max(subd$lnN)]#tmax
  ln.r <- max(diff(subd$lnN) / mean(diff(subd$Time)))
  ln.tLag <- subd$Time[which.max(diff(diff(subd$lnN)))]
  
  c(ln.n0, ln.nMax, ln.r, ln.tLag, ln.tMax)
})

par <- as.data.frame(t(par)) # convert it into a dataframe for convenience
colnames(par) <- c("ln.n0",
                   "ln.nMax", "ln.r", "ln.tLag", "ln.tMax")
#lag time. first approach is to define it as the time to reach 50 or 100% growth, or a factor of .5  or 1. log units increase.


#start values for Logistic model
StartPar_Logistic <- function(id){
  id <- match(id, dID)
  # n0, nMax, r, tLag
  return(list(n0 = par$ln.n0[id], nMax = par$ln.nMax[id], r = par$ln.r[id],
              tLag = par$ln.tLag[id]))
}

StartPar_ModifiedGompertz <- function(id){
  id <- match(id, dID)
  return(list(n0 = par$ln.n0[id], nMax = par$ln.nMax[id], r = par$ln.r[id],
              tLag = par$ln.tLag[id]))
  
}

StartPar_Buchanan <- function(id){
  id <- match(id, dID)
  #n0, nMax, r, tLag, tMax
  return(list(n0 = par$ln.n0[id], r = par$ln.r[id] , tLag = par$ln.tLag[id], tMax = par$ln.tMax[id]))
}

StartPar_Baranyi <- function(id){
  id <- match(id, dID)
  #, n0, nMax, r, tLag
  return(list(n0 = par$ln.n0[id], nMax = par$ln.nMax[id], r = par$ln.r[id] , tLag = par$ln.tLag[id]))
}

fit.Logistic <- sapply(dID, function(x){# 110 fits
  subd <- d[d$ID == x, ]
  tryCatch(nlsLM(lnN ~ Model.Logistic(Time, n0, nMax, r, tLag), data = subd , start = StartPar_Logistic(x),
                 control = nls.lm.control(maxiter = 100)), error = function(e){NA})# substitute error messages with NAs
})

fit.ModifiedGompertz <- sapply(dID, function(x){#298
  subd <- d[d$ID == x, ]
  tryCatch(nlsLM(lnN ~ Model.ModifiedGompertz(Time, n0, nMax, r, tLag), data = subd , start = StartPar_ModifiedGompertz(x),
                 control = nls.lm.control(maxiter = 100)), error = function(e){NA})# substitute error messages with NAs
})

#improper input parameters warnings since the coefficient are too many
fit.Buchanan <- sapply(dID, function(x){
  subd <- d[d$ID == x, ]
  tryCatch(nlsLM(lnN ~ Model.Buchanan(Time, n0, r, tLag, tMax), data = subd , start = StartPar_Buchanan(x),
                 control = nls.lm.control(maxiter = 100)), error = function(e){NA})# substitute error messages with NAs
})

fit.Baranyi <- sapply(dID, function(x){#207 fits
  subd <- d[d$ID == x, ]
  tryCatch(nlsLM(lnN ~ Model.Baranyi(Time, n0, nMax, r, tLag), data = subd , start = StartPar_Baranyi(x),
                 control = nls.lm.control(maxiter = 100)), error = function(e){NA})# substitute error messages with NAs
})

#fitting results for all models
save(fit.Logistic, fit.ModifiedGompertz, fit.Buchanan, fit.Baranyi, file = "../Results/Fittings.RData")


predict.all <- lapply(seq(length(dID)), function(x){# predicting points for all models
  subd <- d[d$ID == dID[x], ]
  time <- subd$Time
  fit <- fit.Logistic[[x]]
  predict <- tryCatch(Model.Logistic(subd$Time, coef(fit)[1], coef(fit)[2], coef(fit)[3], coef(fit)[4]),
                      error = function(e){NA})
  l1 <- data.frame(Predict=predict, Time=time, Model = "Logistic")
  fit <- fit.ModifiedGompertz[[x]]
  predict <- tryCatch(Model.ModifiedGompertz(subd$Time, coef(fit)[1], coef(fit)[2], coef(fit)[3], coef(fit)[4]),
                      error = function(e){NA})
  l2 <- data.frame(Predict=predict, Time=time, Model = "Gompertz")
  fit <- fit.Buchanan[[x]]
  predict <- tryCatch(Model.Buchanan(subd$Time, coef(fit)[1], coef(fit)[2], coef(fit)[3], coef(fit)[4]),
                                    error = function(e){NA})
  l3 <- data.frame(Predict=predict, Time=time, Model = "Buchanan")
  fit <- fit.Baranyi[[x]]
  predict <- tryCatch(Model.Baranyi(subd$Time, coef(fit)[1], coef(fit)[2], coef(fit)[3], coef(fit)[4]),
                      error = function(e){NA})
  l4 <- data.frame(Predict=predict, Time=time, Model = "Baranyi")
  # remove NA rows to avoid plotting error when there is no fitting data
  na.omit(rbind(l1,l2,l3,l4))
}) 


save(predict.all, file = "../Results/Predicts.RData")


RSS <- sapply(seq(length(dID)), function(x){
  subd <- data.frame(Time = d[d$ID == dID[x], ]$Time, lnN = d[d$ID == dID[x], ]$lnN)
  Logistic.rss<- tryCatch(sum(summary(fit.Logistic[[x]])$residuals ^ 2), error = function(e){NA})
  Gompertz.rss <- tryCatch(sum(summary(fit.ModifiedGompertz[[x]])$residuals ^ 2), error = function(e){NA})
  Baranyi.rss <- tryCatch(sum(summary(fit.Baranyi[[x]])$residuals ^ 2), error = function(e){NA})
  Buchanan.rss <- tryCatch(sum(summary(fit.Buchanan[[x]])$residuals ^ 2), error = function(e){NA})
  tempV <- c(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss)
  best.rss <- min(tempV, na.rm = T)
  if(best.rss !=Inf){
    index <-  (tempV == best.rss) * 1
    index <- which(index == 1)##get the index of best model
    Best.model <- Models[index]
  } else{
    Best.model <- NA
  }
  #data.frame(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss, Best.model, stringsAsFactors = F)
  c(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss, Best.model)
  
})

RSS <- as.data.frame(t(RSS))
colnames(RSS) <- c("Logistic.rss", "Gompertz.rss", "Baranyi.rss", "Buchanan.rss", "Best.model")
write.csv(RSS, "../Results/RSS.csv")

AIC <- sapply(seq(length(dID)), function(x){
  subd <- data.frame(Time = d[d$ID == dID[x], ]$Time, lnN = d[d$ID == dID[x], ]$lnN)
  Logistic.AIC<- tryCatch(AIC(fit.Logistic[[x]]), error = function(e){NA})
  Gompertz.AIC <- tryCatch(AIC(fit.ModifiedGompertz[[x]]), error = function(e){NA})
  Baranyi.AIC<- tryCatch(AIC(fit.Baranyi[[x]]), error = function(e){NA})
  Buchanan.AIC <- tryCatch(AIC(fit.Buchanan[[x]]), error = function(e){NA})
  tempV <- c(Logistic.AIC, Gompertz.AIC, Baranyi.AIC, Buchanan.AIC)
  best.AIC <- min(tempV, na.rm = T)
  if(best.AIC !=Inf){
    index <-  (tempV == best.AIC) * 1
    index <- which(index == 1)##get the index of best model
    Smallest.AIC <- Models[index]
    #the difference should be larger than 2
    if(length(which((tempV -best.AIC) > 2 * 1) == 0)){
      Best.model <- "ALL"# there is no statistical significance difference
                                                # in AIC
    }else{
      Best.model <- paste(Models[which(((tempV - best.AIC) >= 2 ) * 1 == 0)], collapse = "")
    }
  } else{
    Best.model <- NA
    Smallest.AIC <- NA
  }
  #data.frame(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss, Best.model, stringsAsFactors = F)
  c(Logistic.AIC, Gompertz.AIC, Baranyi.AIC, Buchanan.AIC, Smallest.AIC, Best.model)
  
})

AIC <- as.data.frame(t(AIC))
colnames(AIC) <- c("Logistic.AIC", "Gompertz.AIC", "Baranyi.AIC", "Buchanan.AIC",
                   "Smallest.AIC", "Best.model")
write.csv(AIC, "../Results/AIC.csv")


#do the same instructions for BIC
BIC <- sapply(seq(length(dID)), function(x){
  subd <- data.frame(Time = d[d$ID == dID[x], ]$Time, lnN = d[d$ID == dID[x], ]$lnN)
  Logistic.BIC<- tryCatch(BIC(fit.Logistic[[x]]), error = function(e){NA})
  Gompertz.BIC <- tryCatch(BIC(fit.ModifiedGompertz[[x]]), error = function(e){NA})
  Baranyi.BIC<- tryCatch(BIC(fit.Baranyi[[x]]), error = function(e){NA})
  Buchanan.BIC <- tryCatch(BIC(fit.Buchanan[[x]]), error = function(e){NA})
  tempV <- c(Logistic.BIC, Gompertz.BIC, Baranyi.BIC, Buchanan.BIC)
  best.BIC <- min(tempV, na.rm = T)
  if(best.BIC !=Inf){
    index <-  (tempV == best.BIC) * 1
    index <- which(index == 1)##get the index of best model
    Smallest.BIC <- Models[index]
    #the difference should be larger than 2
    if(length(which((tempV -best.BIC) > 2 * 1) == 0)){
      Best.model <- "ALL"# there is no statistical significance difference
      # in AIC
    }else{
      Best.model <- paste(Models[which(((tempV - best.BIC) > 2 ) * 1 == 0)], collapse = "")
    }
  } else{
    Best.model <- NA
    Smallest.BIC <- NA
  }
  #data.frame(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss, Best.model, stringsAsFactors = F)
  c(Logistic.BIC, Gompertz.BIC, Baranyi.BIC, Buchanan.BIC, Smallest.BIC, Best.model)
  
})

BIC <- as.data.frame(t(BIC))
colnames(BIC) <- c("Logistic.BIC", "Gompertz.BIC", "Baranyi.BIC", "Buchanan.BIC",
                   "Smallest.BIC", "Best.model")
write.csv(BIC, "../Results/BIC.csv")


#do the same instructions for AICc
AICc <- sapply(seq(length(dID)), function(x){
  subd <- data.frame(Time = d[d$ID == dID[x], ]$Time, lnN = d[d$ID == dID[x], ]$lnN)
  Logistic.AICc<- tryCatch(AICc(fit.Logistic[[x]]), error = function(e){NA})
  Gompertz.AICc <- tryCatch(AICc(fit.ModifiedGompertz[[x]]), error = function(e){NA})
  Baranyi.AICc<- tryCatch(AICc(fit.Baranyi[[x]]), error = function(e){NA})
  Buchanan.AICc <- tryCatch(AICc(fit.Buchanan[[x]]), error = function(e){NA})
  tempV <- c(Logistic.AICc, Gompertz.AICc, Baranyi.AICc, Buchanan.AICc)
  best.AICc <- min(tempV, na.rm = T)
  if(best.AICc !=Inf){
    index <-  (tempV == best.AICc) * 1
    index <- which(index == 1)##get the index of best model
    Smallest.AICc <- Models[index]
    #the difference should be larger than 2
    if(length(which((tempV - best.AICc) > 2 * 1) == 0)){
      Best.model <- "ALL"# there is no statistical significance difference
      # in AIC
    }else{
      Best.model <- paste(Models[which(((tempV - best.AICc) > 2 ) * 1 == 0)], collapse = "")
    }
  } else{
    Best.model <- NA
    Smallest.AICc <- NA
  }
  #data.frame(Logistic.rss, Gompertz.rss, Baranyi.rss, Buchanan.rss, Best.model, stringsAsFactors = F)
  c(Logistic.AICc, Gompertz.AICc, Baranyi.AICc, Buchanan.AICc, Smallest.AICc, Best.model)
  
})

AICc <- as.data.frame(t(AICc))
colnames(AICc) <- c("Logistic.AICc", "Gompertz.AICc", "Baranyi.AICc", "Buchanan.AICc",
                   "Smallest.AICc", "Best.model")
write.csv(AICc, "../Results/AICc.csv")



