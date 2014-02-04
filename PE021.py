""" 
Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n): 
	'''Returns the sum of the proper divisors of n.'''
	divisors = [1] 			#Include 1 to optimize and exclude n.

	i = 2
	while i <= n/i: 
		if n % i == 0: 
			divisors.extend([i, n/i])
		i += 1

	divisors = list(set(divisors)) #Remove duplicates from squares
	return sum(divisors)


amicables = []

for n in range(2, 10000): 
	if n in amicables:
		pass
	else: 
		sumOfProperDivisors = d(n)
		if n == d(sumOfProperDivisors) and n != sumOfProperDivisors: 
			amicables.extend([n, sumOfProperDivisors])


print sum(amicables)