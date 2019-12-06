import re
"""black birds practial"""
# Read the file (using a different, more python 3 way, just for fun!)
with open('../Data/blackbirds.txt', 'r') as f:
    text = f.read()

# replace \t's and \n's with a spaces:
text = text.replace('\t',' ')
text = text.replace('\n',' ')
# You may want to make other changes to the text. 

# In particular, note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform to ASCII:

text = text.encode('ascii', 'ignore') # first encode into ascii bytes
text = text.decode('ascii', 'ignore') # Now decode back to string

# Now extend this script so that it captures the Kingdom, Phylum and Species
# name for each species and prints it out to screen neatly.

# Hint: you may want to use re.findall(my_reg, text)... Keep in mind that there
# are multiple ways to skin this cat! Your solution could involve multiple
# regular expression calls (easier!), or a single one (harder!)


pattern_kingdom = r"Kingdom\sAnimalia\s+([\w,\s]+\w)\s+Phy"
pattern_phylum = r"Phylum\sChordata\s+(\w+,\s\w+,\s\w+)"
pattern_species =  r"Species\s+([\w\s]+\([\w\s\d,]+\)\s+\w+\-\w+\s\w+)|Species\s+([\w\s]+\([\w\s\d,]+\)\s+[\s\w\-\']+\,\s[\s\w\-\']+\,\s[\w\s]{18})"

k = re.findall(pattern_kingdom, text)
p = re.findall(pattern_phylum, text)
s = re.findall(pattern_species, text)

pattern_all = r"Kingdom\sAnimalia\s+([\w,\s]+\w)\s+Phy|Phylum\sChordata\s+(\w+,\s\w+,\s\w+)|Species\s+([\w\s]+\([\w\s\d,]+\)\s+\w+\-\w+\s\w+)|Species\s+([\w\s]+\([\w\s\d,]+\)\s+[\s\w\-\']+\,\s[\s\w\-\']+\,\s[\w\s]{18})"
a = re.findall(pattern_all, text)
           
print(k)
print(p)
print(s)
#######
#parttern_1 = r"\w+\W*\w*\s*\w+\W*\w*\s*"
#parttern_2 = "match abc at the start of string followed by a or b one or more times\
#             Then match a whitespace, a tab and a decimal"
#parttern_3 = "Match a decimal 1 or 2 times at the start of string followed by a  /.\
#             match a decimal 1 or 2 times followed by a /. Match decimal four times at the end of a string"
#parttern_4 = "match whitespace zero or more times match from a-z, A-Z, comma and whitespace one\
#             or more times. match whitespace zero or more times"
#pattern_5 = r"19|20\d{2}(0[1-9])|(1[0-2])[0-3]\d"  