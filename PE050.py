#PE50.py

#Note: Working for the test case; however, run time is terrible for 1,000,000

''' 
The prime 41, can be written as the sum of six consecutive primes: 41 = 2
+ 3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes that adds
to a prime below one-hundred. 

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953. 

Which prime, below one-million, can be written as the sum of the most consecutive primes? 
'''

limit = 1000000

primes = [2, 3]

candidates = set(range(5, limit + 1, 2)) - set(range(6, limit + 1, 3))


def find_best_sequence(prime_list, prime):
	
	candidates = []

	for step in range(2, len(prime_list) + 1):
		for i in range(len(prime_list) - step):

			candidate = sum(prime_list[i:i+step])

			if candidate == prime:
				candidates.append(prime_list[i:i+step])
			elif candidate > prime:
				break 

	if candidates:
		candidates.sort(key=len)
		return candidates[-1]
	else: 
		return [] 

best_candidate = 0
best_sequence = []

for n in candidates:
	for prime in primes:
		if prime > n/prime:
			primes.append(n)
			candidates = candidates - set(range(n*2, limit, n))

			local_candidate_sequence = find_best_sequence(primes, n)
			if len(local_candidate_sequence) > len(best_sequence):
				best_candidate = n
				best_sequence = local_candidate_sequence

			break 

		if n % prime == 0:
			break


print best_candidate, ": ", best_sequence