"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

#For reasons still unclear to me, this is slower than PE005.py; 
#however it's considerably more readable

candidate = 11 * 20
divisors  = range(11, 20)
searching = True

while searching:
	for divisor in divisors:
		if candidate % divisor != 0:
			candidate += 20
			break 
		elif divisor == 19: 
			print candidate 
			searching = False 
