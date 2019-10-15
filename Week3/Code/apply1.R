
## Build a random matrix
M <- matrix(rnorm(100), 10 ,10)

## Take the mean of each row
RowMeans <- apply(M, 1, mean) #MARGIN 1 indicates rows and 2 indicates columns
print (RowMeans)

## Now the variance
RowVars <- apply(M, 1, var)
print (RowVars)

## By column
ColMeans <- apply(M, 2, mean)
print (ColMeans)
