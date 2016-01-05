#PE35.py
"""
How many circular primes are there below one million? 
"""

from euler_functions import generate_primes_less_than as g

primes = set(g(10**6)) # Convert to set for faster comparison

circular = 0

for prime in primes:
    prime = str(prime)
    # Collect rotations and cast them to set so we can use issubset
    rotations = set([int(prime[i:] + prime[:i]) for i, d in enumerate((prime))])
    if rotations.issubset(primes):
        circular += 1

print circular
