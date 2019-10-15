
loop_dynamic <-function(x){##relocate memory every iteration
  a <- NA
  for (i in 1:x) { 
    a <- c(a, i)
   # print(a)
    #print(object.size(a))
  }
}

loop_prealloc <- function(x){
  a <- rep(NA, x)##preallocate memory space for vector a
  for (i in 1:x) {
    a[i] <- i
    #print(a)
    #print(object.size(a))
  }
}

print("Without pre-allocating memory space, the time taken is:")
print(system.time(loop_dynamic(10000)))
print("When using pre-allocation, the time taken is:")
print(system.time(loop_prealloc(10000)))