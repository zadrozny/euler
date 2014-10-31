"""
Project Euler Problem #50
==========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from euler_functions import is_prime

#  Initialize with some primes to see the pattern
#  primes = {prime: {number of preceding primes: sum of preceding primes}}

primes = 	{2:  {0:  0}, 
			 3:  {1:  2}, 
			 5:  {2:  5,  1:  3}, 
			 7:  {3: 10,  2:  8,  1:  5}, 
			 11: {4: 17,  3: 15,  2: 12,  1:  7},
			 13: {5: 28,  4: 26,  3: 23,  2: 18,  1: 11}
			 }



def find(limit):
	
	'''
	Find prime below limit that can be written as
	the sum of the most consecutive primes.
	'''
	
	previous_prime = 13
	candidate = 15      # previous_prime + 2
	best_streak = 4     # 2 + 3 + 5 + 7 = 17
	best_prime = 17     # ie, has the longest streak 

	while candidate < limit: # 1000000:

		if is_prime(candidate):

			value = {prime + 1: primes[previous_prime][prime] + 
						previous_prime for prime in primes[previous_prime]}																																																												
			
			value[1] = previous_prime # Add preceding prime to the list


			candidate_streak = best_streak + 1

			while candidate_streak in value:

				embedded_candidate = value[candidate_streak]
			
				if embedded_candidate > limit:
					return best_prime

				elif is_prime(embedded_candidate):
					best_streak = candidate_streak
					best_prime = embedded_candidate
				
				candidate_streak += 1
			
			primes[candidate] = value # Append the primes list
			previous_prime = candidate

		candidate += 2

	return best_prime


limit = 1000000	# "...which prime, below one million..."

print find(limit)
