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

from euler_functions import generate_next_prime, is_prime

#  Initialize with some primes to see the pattern:
#  primes = {prime: {previous n primes: sum of previous n primes, 
# 					 previous n -1 primes: sum of previous n - 1 primes}
# 			}

primes = 	{2:  {0:  0}, 
			 3:  {1:  2}}



def find(limit):
	'''
	Find prime below limit that can be written as
	the sum of the most consecutive primes.
	'''
	
	previous_prime = 2

	best_streak = 0    # 2 + 3 = 5
	best_prime = 0     # ie, has the longest streak 

	g = generate_next_prime(start=5) 

	candidate = next(g)

	while candidate < limit: # 1000000:
		
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

		candidate = next(g) # Generate next prime

	return best_prime


limit = 1000000	# "...which prime, below one million..."

print find(limit)
