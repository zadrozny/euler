def factorize(n):
	'''Return the prime factors of a number, n.'''

	if n in [0, 1]:
		return []

	primes = generate_primes_less_than(n + 1)
	factors = []
	for prime in primes:
		if n % prime == 0:
			factors.append(prime)
			n = n / prime

	return factors



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

	prime_list = [] 					#Intialize with 2 to skip evens.

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

