#!/usr/bin/env python3
#FIND just those taxa that are oak trees from a list of species

taxa = [
    'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
]

def is_an_oak(name):
    return name.lower().startswith("quercus ")

##using for loops
oaks_loops = set()

for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)
print(oaks_loops)

##using list comprehensions
oaks_lc=set([species for species in taxa if is_an_oak(species)])
print(oaks_lc)

##get names in uppercase using for loops
oaks_loops = set()

for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper())
print(oaks_loops)

##get names in uppercase using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print(oaks_lc)
