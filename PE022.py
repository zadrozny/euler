"""
What is the total of all the name scores in the file 
[wherein a name has a value corresponding to the multiple of its 
alphabetical position and the sum of the positions of its characters
in the alphabet]? 
"""

from urllib import urlopen
import string

letter_vals = {let: i for i, let in enumerate(string.uppercase, 1)}

f = urlopen("https://projecteuler.net/project/resources/p022_names.txt")
names = f.readlines()
names = [name.strip("\n").strip('"') for name in names[0].split(',')]
names.sort()

print sum([sum([letter_vals[let] for let in name]) * pos 
	       for pos, name in enumerate(names, 1)])
