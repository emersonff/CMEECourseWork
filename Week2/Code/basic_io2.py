############################File Output
#save the elements of a list to a file
list_to_save = range(100)

f = open("../Sandbox/testout.txt", "w")
for i in list_to_save:
    f.write(str(i) + "\n")#add new line at the end

f.close()
