#PE10.py
"""
Find the sum of all the primes below two million. 
"""

prime_list = [2] 	# Intialize with 2 to skip evens.

for candidate in xrange(3, 2000000, 2): 		
    for prime in prime_list:			
        if candidate % prime == 0:			# It's not prime.
            break	
        if prime > candidate/prime: 		# It is prime.
            prime_list.append(candidate) 	
            break				
		
print sum(prime_list)
