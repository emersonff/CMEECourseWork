import csv

#Read a file containing:
#"Spicies","Infraorder","Family","Distribution", "Body mass male(Kg)"
f = open("../Data/testcsv.csv", "r")

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("The species is ", row[0])

f.close()

#write a file containing  only species name and Body mass
f = open("../Data/testcsv.csv","r")
g = open('../Data/bodymass.csv','w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    #print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()

#read bodymass file
f = open("../Data/bodymass.csv","r")
csvread =csv.reader(f)
for row in csvread:
    print(row[0], " ", row[1])

f.close()