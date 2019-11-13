#!usr/bin/env python3
"""regular expression in python"""
__appname__ = "regexs"
__author__ = "Xiang Li(xiang.li419@imperial.ac.uk)"
__version__ = "0.0.1"
__license__ = "none"

###imports
import re
import urllib3

#globals
my_string = "a given string"
match = re.search(r"\s", my_string)
print(match)
match = re.search(r"\d", my_string)# none cause no numeric characters
print(match)
MyStr = "an example"
match = re.search(r"\w*\s", MyStr)
if match:
    print("found a match:", match.group())
else:
    print("did not find a match")

match = re.search(r"2", "it takes 2 to tango")
match.group()

match = re.search(r"\d", "it takes 2 to tango")
match.group()

match = re.search(r'\d.*' , "it takes 2 to tango")
match.group()

match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

match = re.search(r'\s\w*$', 'once upon a time')
match.group()

re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()

re.search(r'^\w*.*?\s', 'once upon a time').group()

re.search(r'<.+>', 'This is a <EM>first</EM> test').group()

re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()

re.search(r'\d*\.?\d*','1432.75+60.22i').group()

re.search(r'\s+[A-Z]\w+\s*\w+', "The bird-shit frog's name is Theloderma asper.").group()

MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory'

match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s]+", MyStr)
match.group()

MyStr = 'Samraat Pawar, s-pawar@imperial.ac.uk, Systems biology and ecological theory'

match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s&]+",MyStr)
match.group()



match = re.search(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+),\s([\w\s&]+)",MyStr)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))


###finding all matches
MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk,\
 Systems biology and ecological theory; Another academic,\
  a-academic@imperial.ac.uk, Some other stuff thats equally boring;\
   Yet another academic, y.a_academic@imperial.ac.uk, Some other stuff thats even more boring"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', MyStr) 
for email in emails:
    print(email)

#finding in files
f = open('../Data/TestOaksData.csv', 'r')
found_oaks = re.findall(r"Q[\w\s].*\s", f.read())

found_oaks

###group within multiple matches


MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory; Another academic, a.academic@imperial.ac.uk, Some other stuff thats equally boring; Yet another academic, y.a.academic@imperial.ac.uk, Some other stuff thats even more boring"

found_matches = re.findall(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+)", MyStr)
found_matches

for item in found_matches:
    print(item)


###extracting text from web pages
conn = urllib3.PoolManager() # open a connection
r = conn.request('GET', 'https://www.imperial.ac.uk/silwood-park/academic-staff/') 
webpage_html = r.data #read in the webpage's contents
#type(webpage_html) is bytes
My_Data  = webpage_html.decode() # decoding with utf-8 as default method
#print(My_Data)
pattern = r"(Dr|Prof|Professor)\s+(\w+[\-`']?\w+\s+\w+[`\-']?\w+)" # pattern for names
regex = re.compile(pattern) # example use of re.compile(); you can also ignore case  with re.IGNORECASE 
for match in regex.findall(My_Data): # example use of re.findall()
    print(match)

###replacing text
New_Data = re.sub(r'\t'," ", My_Data) # replace all tabs with a space
# print(New_Data)




