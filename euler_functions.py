#from __future__  import division
from operator import mul
from itertools import combinations


def factorial(n):
	'''Return the factorial of a number.'''
	return 1 if n == 0 else multiply(range(1, n+1))



def factorize(n):
	'''Return prme factors of a number'''

	if n <= 0:
		raise ValueError("n must be greater than 0.")

	if n % 2 == 0:
		prime_factors = [2]

	else:
		prime_factors = []


	divisor = 3  # Because n is odd, start with 3 and not 2

	while divisor <= n:

		if n % divisor == 0: 

			prime_factors.append(divisor)

			n = n / divisor  			  # Update n to prevent redundancy

			if n % divisor == 0:		  #Remove powers of a number
				while n % divisor == 0:
					n = n / divisor

		divisor += 2  # Since all prime > 2 are odd

	return prime_factors



def generate_n_primes(n):
	'''Generates a list of n primes'''
	if n == 0:
		return []

	prime_list = [2] 					#Intialize with 2 to skip evens.

	for n in xrange(3, n, 2): 			#Skip evens.	
		for p in prime_list:			
			if n%p == 0:			 	#It's not prime.
				break	
			if p > n/p: 			 	#It is prime.
				prime_list.append(n) 	
				break				
				
	return prime_list



def generate_next_prime():
	'''Generates next prime, ad infinitum.'''

	prime_list = [] 					

	if len(prime_list) == 0:
		prime_list.append(2)
		yield 2
	if len(prime_list) == 1:
		prime_list.append(3)
		yield 3

	n = prime_list[-1]
	while True: 
		n += 2	
		for p in prime_list:			
			if n%p == 0:			 	#It's not prime.
				break	
			if p > n/p: 			 	#It is prime.
				prime_list.append(n) 
				yield n 	
				break

			

def generate_primes_less_than(n):
	'''Generates a list of primes less than n.'''
	if n <= 2:
		return []

	if n <= 3:
		return [2]

	prime_list = [2, 3] 					#Intialize with 2 to skip evens.
	
	if n <= 5:
		return prime_list

	candidate = 5
	while True:
		for p in prime_list:			
			if candidate % p == 0:			 	# It's not prime.
				break	

			if p > candidate / p: 				# It is prime.
				
				if candidate > n:
					return prime_list

				prime_list.append(candidate) 	
				break							# Break out of for loop, 									  increment candidate

		candidate += 2			 				# Skip evens.					
				
	return prime_list



def is_prime(candidate):
	'''Return True if prime and False if not.'''
	if candidate <= 0:
		raise ValueError("Integer must be > 0")

	if candidate == 1:
		return False 
		
	if candidate == 2:
		return True
	
	if candidate == 3:
		return True

	if candidate % 2 == 0:
		return False

	divisor = 3
	while divisor <= candidate / divisor:
		if candidate % divisor == 0:
			return False
		divisor += 2

	return True 



def multiply(lst):
	'''Return the product of a list.'''
	if type(lst) != list:
		raise Exception("You need a list. You entered a: ", type(lst))

	product = 1 
	for term in lst:
		product *= term
	return product 



def n_choose_k(n, k):
	'''Return the number of k combinations given a set of n elements: n! / k!*(n-k)!'''
	return factorial(n) / (factorial(k) * factorial(n - k))

