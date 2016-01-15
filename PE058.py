"""
Project Euler Problem #58
==========================

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33 32 31
                           38 17 16 15 14 13 30
                           39 18  5  4  3 12 29
                           40 19  6  1  2 11 28
                           41 20  7  8  9 10 27
                           42 21 22 23 24 25 26
                           43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

from __future__ import division
from euler_functions import is_prime


def generate_diagonals():
	
    diagonals = [1, 3, 5, 7, 9] # Initialize

    primes = [n for n in diagonals if is_prime(n)]

    side_length = 3 # Equivalent to sqrt(diagonals[-1])

    while True:
        side_length += 2 # Adding 2 gives 'one complete new layer' (not half)

        for _ in range(4): # Four new diagonals each time
			
            diagonal = diagonals[-1] + side_length - 1
			
            diagonals.append(diagonal)

            if is_prime(diagonal):
                primes.append(diagonal)

        yield (side_length, len(primes), len(diagonals))




g = generate_diagonals()

while True:
    side_length, num_of_primes, num_of_diagonals = next(g)

    ratio = num_of_primes / num_of_diagonals

    if ratio < 0.10:
        print "side_length: ", side_length
        break 
