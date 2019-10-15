SomeOperation <- function(v){ ## if the sum of all elements in v is positive, return v with every element in it  multipling 100.
  if(sum(v) >0){              ## otherwise return v
    return (v * 100)
  }
  return (v)
}

M <- matrix(rnorm(100), 10, 10)
print(apply(M, 1, SomeOperation))