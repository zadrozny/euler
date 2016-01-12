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

from euler_functions import generate_next_prime 
from collections import defaultdict

p = generate_next_prime()      # Prime generator

candidates = defaultdict(list) # Candidate primes, stored by digit hash

candidate = next(p)            # The first prime: 2
while candidate < 1000:        # Get the first 4-digit prime
	candidate = next(p)        # Avoid `if candidate > 999` in next while loop


while True:
    key = tuple(sorted(str(candidate)))
    candidates[key].append(candidate)
    if len(candidates[key]) >= 3:
        # Check for sequence:                          
        if candidates[key][-1] - candidates[key][-2] == \
           candidates[key][-2] - candidates[key][-3]:
            print ''.join(map(str, candidates[key][-3:]))
            break                    	
    candidate = next(p)
