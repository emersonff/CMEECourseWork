# A simple script to illustrate R input-output.
# run line by line and check inputs and outputs to understand what is happening

MyData <-read.csv("../Data/trees.csv", header = TRUE)#imports with headers.Tho the default value for header is TRUE already
write.csv(MyData, "../Results/MyData.csv") #write it out as a new file default value of row.names and col.names are both TRUE.
write.table(MyData[1,], file="../Results/MyData.csv", append = TRUE)#Append header(first row) to the file
write.csv(MyData, "../Results/MyData.csv", row.names = TRUE)#write row names.
write.table(MyData, "../Results/MyData.csv", col.names = FALSE)#ignore column names
