rm(list = ls())
library(maps)
library(ggplot2)

gpdd <- get(load("../Data/GPDDFiltered.RData"))# load data
WorldData <- map_data("world") # turn world2 data from maps package into a dataframe for plotting with ggplot2
p <- ggplot() + geom_map(data = WorldData, map = WorldData,
           aes(x = long, y = lat, group = group, map_id=region),
           fill = "white", colour = "#7f7f7f", size=0.5) #plot world map

p <- p + geom_point(aes(x=gpdd$long, y=gpdd$lat) ,color="blue", size=1)#insert locations
#save in pdf
pdf("../Results/GPDD_Result.pdf")
p
graphics.off()
### expecting:locations are bias towards higher latitude(around 50) and coastal region