"""
Project Euler Problem #26
==========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

from decimal import *
getcontext().prec = 10000 # The smallest precision to capture the cycle


def generate_decimals(d):
	'''Returns a string of decimals for 1/d.'''
 	return str(Decimal(1) / Decimal(d))[2:]


def find_subsequences(n):
	'''Finds sub-cycles within a cycle, eg, 01 from 01010101. '''
	for i in range(len(n)/2):
		if len(n)/(i+1) * n[:i+1] == n:
			return i + 1
	return len(n)


def find(n):
	'''Finds the longest potential cycle in a sequence.'''

	for window in range(len(n)/2, 0, -1): # Best case: cycle is half the sequence

		for start in range(0, (len(n) - 2*window + 1 )):

			if 2 * n[start:window+start] in n:

				# Ensure it's not one short, recurring cycle:
				return find_subsequences(n[start:window + start])



best_d = 0        # The best denominator
longest_recurring_cycle = 0 # Length of cycle for the best denominator

for n in range(1, 1000):
	candidate = generate_decimals(n)
	candidate_longest = find(candidate)
	if candidate_longest > longest_recurring_cycle:
		longest_recurring_cycle = candidate_longest
		best_d = n


print 'The value of d that produces the longest recurring cycle is', best_d
print 'The longest recurring cycle has a length of:', longest_recurring_cycle
