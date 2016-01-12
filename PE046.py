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


from euler_functions import is_prime, generate_next_prime 
# generate_primes_less_than


def check(n):
    '''Check whether n can be written as the sum 
	of a prime and twice a square'''

    # primes = generate_primes_less_than(n)

    for p in primes: 
        i = 1
        total = 0
        while total < n:
            total = p + 2 * i**2
            i+=1
        if total == n:
            return True           # Can be written
    return False                  # Cannot be written


g = generate_next_prime()
primes = {next(g) for i in range(3)} # Seed with 2, 3, 5

n = 3
while True: 
    p = next(g)
    primes.add(p)
    if n in primes:
        pass	
    elif check(n) == False: 
        print n
        break 
    n+=2 			# Check only odds


