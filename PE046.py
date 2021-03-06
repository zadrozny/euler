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

from euler_functions import generate_next_prime 


def check(n):
    '''Check whether n can be written as the sum 
	of a prime and twice a square'''

    for p in primes: 
        i = 1
        total = 0
        while total < n:
            total = p + 2 * i**2     # Sum of prime and twice a square
            i+=1
        if total == n:
            return True              # Can be written
    return False                     # Eureka! Cannot be written


p = generate_next_prime()            # Prime generator
primes = {next(p) for i in range(3)} # Seed with 2, 3, 5

n = 3                                # First odd to check
while True: 
    primes.add(next(p))
    if n in primes:                  # Not a composite
        pass	
    elif check(n) == False: 
        print n                      # Found it!
        break 
    n+=2                             # Check next odd
