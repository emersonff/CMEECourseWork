library(minpack.lm)
library(dplyr)
rm(list = ls())#clear workspace

#read data
d <- read.csv("../Data/NewData.csv", header = T)
dID <- unique(d$ID)

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
  sapply(t, function(x){
    if(x <= tLag){#lag phase
      n0
    }else if(x >= tMax){# stationary phase
      #nMax
      n0 + r * (tMax - tLag)
    }else{#exponential growth phase
      n0 + r * (x - tLag)
    }
  })
  
  #return(n0 + (t >= tLag) * (t <= (tLag + (nMax - n0) * log(10)/r)) * 
   #        r * (t - tLag)/log(10) + (t >= tLag) *
    #       (t > (tLag + (nMax - n0) * log(10)/r)) * (nMax - n0))
}

Model.Baranyi <- function(t, n0, nMax, r, tLag){
  h0 <- tLag * r
 # at <- (1 / r) * log(exp(- r * t) + exp(-h0) - exp(- r * t - h0))
 # return(n0 + r * t + at - log(1 + (exp(r * t + at) - 1) / (exp(nMax - n0))))
  at <- t + log(exp(-r * t) + exp(-h0) - exp(-r * t - h0)) / r
  return(n0 + r * at - log(1 + (exp(r * at) - 1) / exp(nMax - n0)))

  
}


par <- sapply(dID, function(x){
  subd <- data.frame(Time = d[d$ID == x, ]$Time, PopBio = d[d$ID == x, ]$PopBio,
                     lnN = d[d$ID == x, ]$lnN)#subset according to ID.
  n0 <- subd$PopBio[1]
  nMax <- max(subd$PopBio)
  tMax <- subd$Time[which.max(subd$PopBio)]#tmax
  r <- max(diff(subd$PopBio) / mean(diff(subd$Time)))
  #r <- max(diff(subd$PopBio) / diff(subd$Time))x
  #tLag <- subd$Time[which.max(diff(subd$PopBio) / diff(subd$Time))]
  tLag <- subd$Time[which.max(diff(diff(subd$PopBio)))]
  
  ln.n0 <- subd$lnN[1]
  ln.nMax <- max(subd$lnN)
  ln.tMax <- subd$Time[which.max(subd$lnN)]#tmax
  ln.r <- max(diff(subd$lnN) / mean(diff(subd$Time)))
  ln.tLag <- subd$Time[which.max(diff(diff(subd$lnN)))]
  
  c(n0, nMax, r, tLag, tMax, ln.n0, ln.nMax, ln.r, ln.tLag, ln.tMax)
})

par <- as.data.frame(t(par))
colnames(par) <- c("n0", "nMax", "r", "tLag", "tMax", "ln.n0",
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

save(fit.Logistic, fit.ModifiedGompertz, fit.Buchanan, fit.Baranyi, file = "../Data/Fittings.RData")


predict.all <- lapply(seq(length(dID)), function(x){
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

#predict.all <- rbind(t(predict.Baranyi),t(predict.Buchanan),t(predict.Logistic),t(predict.ModifiedGompertz))
save(predict.all, file = "../Data/Predicts.RData")

