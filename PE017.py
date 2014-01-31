#PE17.py
"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used [not counting spaces or hyphens, but using "and"]? 
"""

digits = ["one", "two", "three", "four", "five", 
			"six", "seven", "eight", "nine"] 

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
		"sixteen", "seventeen", "eighteen", "nineteen"]

doubles = ["twenty", "thirty", "forty", "fifty", 
			"sixty", "seventy", "eighty", "ninety"]


def convert(n):
	'''Converts numbers up to 1000.'''
	length = len(str(n))

	if length == 1:
		return digits[n - 1] 

	elif length == 2:
		if n < 20:
			return teens[n - 10]
		elif n%10 == 0:
			return doubles[int(str(n)[0])-2]			
		else: 
			return doubles[int(str(n)[0]) - 2] + '-' + digits[int(str(n)[1]) - 1] 

	elif length == 3:
		if n % 100 == 0: 
			return convert(int(str(n)[0])) + '-hundred'
		else: 
			return convert(int(str(n)[0])) + '-hundred' + ' and ' + convert(int(str(n)[1:]))

	elif length == 4:    
		if n % 1000 == 0: 
			return convert(int(str(n)[0])) + '-thousand'


def count(string):
	return len([x for x in string if x != '-' and x != ' '])


total = 0 
for n in range(1, 1001): 
	total += count(convert(n))


print total 