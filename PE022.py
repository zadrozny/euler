"""
What is the total of all the name scores in the file 
[wherein a name has a value corresponding to the multiple of its 
alphabetical position and the sum of the positions of its characters
in the alphabet]? 
"""

import string

alpha = string.uppercase

letterValues = {}

for i, letter in enumerate(alpha): 
	letterValues[letter] = i + 1


f = #Insert path to file with names

with open(f, "r") as f: 
	names = f.readlines()


names = [name.strip("\"") for name in names[0].split(',')]

names.sort()


total = 0
for i, name in enumerate(names): 
	position = i + 1
	value    = sum([letterValues[letter] for letter in name])
	score    = position * value
	total   += score 


print total 