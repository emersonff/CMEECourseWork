M <- matrix(runif(1000000), 1000, 1000)

SumAllElements <- function(M){##sum all elements in matrix M
  Dimensions <- dim(M)
  Tot <- 0
  for(i in 1:Dimensions[1]){
    for(j in 1:Dimensions[2]){
      Tot <-Tot + M[i, j]
    }
  }
  return (Tot)
}

print("USing loops, the time taken is:")
print(system.time(SumAllElements(M)))

print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M)))



