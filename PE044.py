"""
Project Euler Problem #44
==========================

Pentagonal numbers are generated by the formula, P[n]=n(3n-1)/2. The first
ten pentagonal numbers are:

               1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
and difference is pentagonal and D = |P[k] - P[j]| is minimised; what is
the value of D?
"""

from itertools import combinations

def generate_pentagonal(n):
	return n * (3 * n - 1)/2

#Storing in a dictionary means a runtime of ~5 secs; list takes much longer
#The range is arbitrary at present (though it does return the correct answer)
pentagonals = {generate_pentagonal(n) for n in range(1, 10000)}

for candidate in list(combinations(pentagonals, 2)):
	if candidate[0] + candidate[1] in pentagonals:
		if candidate[1] - candidate[0] in pentagonals:
			print candidate[1] - candidate[0]


