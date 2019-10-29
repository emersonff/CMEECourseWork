a<-read.table("../Data/ObserverRepeatability.txt",  header=T) 	
require(dplyr) 	
a  %>%  group_by(StudentID)  %>% 	summarise  (count=length(StudentID))
a  %>%  group_by(StudentID)  %>% 	summarise  (count=length(StudentID)) %>% summarise(length(StudentID))

a  %>%  group_by(StudentID)  %>% 	summarise  (count=length(StudentID)) %>% summarise(sum(count))
length(a$StudentID) 	
a  %>%  group_by(StudentID)  %>% 	summarise  (count=length(StudentID)) %>% summarise(sum(count^2))
