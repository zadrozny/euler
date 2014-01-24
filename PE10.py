#PE10.py
"""
Find the sum of all the primes below two million. 
"""

prime_list = [2] 					#Intialize with 2 to skip evens.


for n in xrange(3, 2000000, 2): 		
	for p in prime_list:			
		if n%p == 0:			 	#It's not prime.
			break	
		if p > n/p: 			 	#It is prime.
			prime_list.append(n) 	
			break				
			

print sum(prime_list)