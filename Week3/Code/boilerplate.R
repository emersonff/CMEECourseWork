# A boilerplate R script

MyFunction <- function(Arg1, Arg2){
  #Statements involving Arg1, Arg2:
  print(paste("Argument", as.character(Arg1), "is a", class(Arg1)))#print type
  print(paste("Argument", as.character(Arg2), "is a", class(Arg1)))#print type
  
  return (c(Arg1, Arg2))#optional but useful
}

MyFunction(1,2)
MyFunction("Riki", "Tiki")