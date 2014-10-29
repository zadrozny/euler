#PE4.py
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers
'''

upper = 999
lower = 100
best  = 0

for x in xrange(upper, lower, -1):
	for y in xrange(x, lower, -1):
		multiple = str(x*y)
		if multiple == multiple[::-1]: # Check if palindrome
			if x*y > best: 
				best = x*y 

print best 
