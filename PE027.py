"""
Project Euler Problem #27
==========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                                e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

from euler_functions import is_prime

def calc_quad(n, a, b):
    '''Calculate n**2 + a*n + b.'''
    return n**2 + a*n + b 

primes = [n for n in range(1, 1000, 2) if is_prime(n)] # Potential values of b

best_n, best_a, best_b, prime_record = None, None, None, None

for a in range(-999, 1000):
    for b in primes:		# At a = 0, b must be a prime.
        prime_list = []
        n = 0
        while True:
            candidate = calc_quad(n, a, b)
            if candidate > 1 and is_prime(candidate):
                prime_list.append(candidate)
                n+=1
            else:
                break

        primes_produced = len(prime_list) 

        if primes_produced > prime_record:
            best_n, best_a, best_b, prime_record = n, a, b, primes_produced

print best_a*best_b