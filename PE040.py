#PE40.py
''' 
Problem 40: Champernowne's constant 

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021... 

It can be seen that the 12th digit of the fractional part is 1. 

If dn represents the nth digit of the fractional part, 
find the value of the following expression. 

d1*d10*d100*d1000*d10000*d100000*d1000000 
'''


limit = 1000000 

s 	  = ''

for n in xrange(limit):
	s += str(n)


product = 1 

i = 1
while i <= limit:
	product *= int(s[i])
	i *= 10

print product 