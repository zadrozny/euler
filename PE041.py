#Note to self. Probably have algorithm, but it's taking too long.

'''Problem 41: Pandigital prime 

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime. 

What is the largest n-digit pandigital prime that exists?
'''
#7652413
from itertools import permutations

def test_for_primeness(contender):
	i = 2
	while i <= contender / i: 
		if contender % i == 0:
			return False
		i += 1
	return True  


digits = '123456789'
primes = []

while not primes: 
	for candidate in permutations(digits):
		candidate = int(''.join(candidate))

		if test_for_primeness(candidate):
			primes.append(candidate)

	digits = digits[:-1] #Remove a digit if necessary

print primes[-1]