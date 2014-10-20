"""
Project Euler Problem #46
==========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""


from euler_functions import is_prime, generate_primes_less_than

def check(n):
	'''Check whether n can be written as the sum 
	of a prime and twice a square'''

	primes = generate_primes_less_than(n)

	for prime in primes: 
		i = 1
		total = 0
		while total < n:
			total = prime + 2 * i**2
			i+=1
		if total == n:
			return True # Can be written

	return False # Cannot be written


n = 9
while True: 

	if is_prime(n):
		pass
	
	elif check(n) == False: 
		print n
		break 

	n+=2 			# Check only odds


