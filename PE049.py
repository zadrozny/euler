"""
Project Euler Problem #49
==========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from euler_functions import is_prime


def check_distances(primelist):
    for x, prime_one in enumerate(primelist):
        for y, prime_two in enumerate(primelist[x+1:]):
            for prime_three in primelist[y+1:]:
                if prime_three - prime_two == prime_two - prime_one:
                    print str(prime_one)+str(prime_two)+str(prime_three)


primes = {}
for n in range(1001, 10000, 2):
    if is_prime(n):
        key = ''.join(sorted(list(str(n))))
        if key in primes:
            primes[key].append(n)
            if len(primes[key]) >= 3:
                check_distances(primes[key])
        else:
            primes[key] = [n]

