#PE35.py
"""
How many circular primes are there below one million? 
"""


prime_list = [2] 					#Intialize with 2 to skip evens.

for n in xrange(3, 1000000, 2): 		
	for p in prime_list:			
		if n%p == 0:			 	#It's not prime.
			break	
		if p > n/p: 			 	#It is prime.
			prime_list.append(n) 	
			break				
			
prime_list = set(prime_list)



circular_primes = []

for prime in prime_list:
	prime = str(prime)
	rotations = set([int(prime[i:] + prime[:i]) for i, d in enumerate((prime))])
	if rotations.issubset(prime_list):
		circular_primes.append(prime)


print len(circular_primes)