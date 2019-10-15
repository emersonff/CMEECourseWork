##If statement
a <- TRUE
if (a == TRUE){
  print("a is true")
  }else{
  print("a is false")
}

##If statement in a single line
z <- runif(1)##uniformly distributed random number
if(z <= 0.5){print("Less than a half")}

##For loop using a sequence
for(i in 1:10){
  j <- i * i
  print(paste(i, " squared is", j))##pastes elements together using space
}

##For loop over vector of strings
for(species in c("Heliodoxa rubinoides", 'Boissonneaua jardini', 'Sula nebouxii')){
  print(paste("The species is", species))
}

##For loop using a vector
v1 <- c("a", "bc", "def")
for(i in v1){
  print(i)
}

##While loop
i <-0
while(i < 10){
  i <- i +1
  print(i^2)
}

