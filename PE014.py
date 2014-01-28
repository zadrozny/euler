#PE14.py
''' 
The following iterative sequence is defined for the set of positive
integers: n --> n/2 (n is even) n --> 3n + 1 (n is odd). 

Which starting number, under one million, produces the longest chain?
''' 

def findLength(n):

	length = 1 					 #For n=1, length=1
	while n != 1: 
		if n%2 == 0: n = n/2
		else:  	     n = 3*n + 1
		length += 1

	return length


startingNumber = 0
longestChain   = 0

for n in xrange(1, 1000000):
	candidate = findLength(n)
	if candidate > longestChain:
		longestChain   = candidate
		startingNumber = n


print startingNumber, longestChain
