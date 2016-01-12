"""
PE Problem #47
==========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

# Runtime: 85s

# Two of the numbers will be even and two will be odd
# One of the evens will be divisible by 4


from euler_functions import factorize

consecutive_integers = 0
i = 1
while consecutive_integers < 4:
    if len(factorize(i)) == 4:
        consecutive_integers += 1
    else: 
        consecutive_integers = 0
    i+=1

print i - 3 - 1 # Subract 3 because it is the 4th and 1 for i+=1


