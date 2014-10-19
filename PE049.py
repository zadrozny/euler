def check_primality(n):
	'''Checks if odd number > 2 is prime'''
	i = 3
	while i <= n/i:
		if n % i == 0: return False
		i+=2
	return True

def check_distances(primelist):
	for x, prime_one in enumerate(primelist):
		for y, prime_two in enumerate(primelist[x+1:]):
			for prime_three in primelist[y+1:]:
				if prime_three - prime_two == prime_two - prime_one:
					print str(prime_one)+str(prime_two)+str(prime_three)

primes = {}
for n in range(1001, 10000, 2):
	if check_primality(n):
		key = ''.join(sorted(list(str(n))))
		if key in primes:
			primes[key].append(n)
			if len(primes[key]) >= 3:
				check_distances(primes[key])
		else:
			primes[key] = [n]
