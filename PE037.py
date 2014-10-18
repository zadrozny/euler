"""
Project Euler Problem #37
==========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def isprime(candidate):
    '''Returns True if prime and False if not'''

    if candidate == 1:
        return False 

    if candidate == 2:
        return True
    
    if candidate == 3:
        return True

    if candidate % 2 == 0:
        return False

    divisor = 3
    while divisor <= candidate / divisor:
        if candidate % divisor == 0:
            return False
        divisor += 2
    return True 


primes = []

candidate = 23
while len(primes) < 11: 
    if isprime(candidate):
        s = str(candidate)
        truncations = [s[i:] for i in range(1, len(s))] + \
                        [s[:-i] for i in range(1, len(s))]

        for truncation in truncations:
            if isprime(int(truncation)) == False:
                break 
        else: 
            primes.append(candidate)

    candidate += 2


print primes 
print sum(primes)