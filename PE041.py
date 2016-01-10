#Note to self. Probably have algorithm, but it's taking too long.

'''Problem 41: Pandigital prime 

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime. 

What is the largest n-digit pandigital prime that exists?
'''

from euler_functions import is_prime
from itertools import permutations

digits = '123456789'
primes = []

while not primes: 
    for candidate in permutations(digits):
        candidate = int(''.join(candidate))
        if is_prime(candidate):
            primes.append(candidate)
    digits = digits[:-1] #Remove a digit if necessary

print primes[-1]