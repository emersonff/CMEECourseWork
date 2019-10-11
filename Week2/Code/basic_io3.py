############################Storing objects
#to save an object for later use
my_dictionary={"a key": 10, "another key": 11}

import pickle

f =open("../Sandbox/testp.p","wb")#b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

#load the data again
f =open("../Sandbox/testp.p", "rb")
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)
