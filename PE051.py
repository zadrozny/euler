"""
Project Euler Problem #51
==========================

By replacing the 1^st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

from euler_functions import generate_next_prime, is_prime
from itertools import combinations


primes = generate_next_prime() # Infinite generator


def replace(n, new_digit, *indices):
    lst = list(str(n))
    for i in indices:
        if lst[i] != str(new_digit):
            lst[i] = str(new_digit)
        else: 
            return None
    return int(''.join(lst))


def test(prime, number_of_primes=8):
    length = len(str(prime)) # Number of digits in the prime

    primes_list = [prime]

    # How many digits are we replacing?
    for num in range(1, length + 1): 
		
        # Which digits are we replacing?
        for comb in combinations(range(length), num): 

            # Which digit are we replacing it with?
            for d in range(1,10): 
			
                candidate = replace(prime, d, *comb)

                try: 
                    if is_prime(candidate):
                        if candidate not in primes_list:
                            primes_list.append(candidate)
                except ValueError:
                    pass 
				
                if len(primes_list) == number_of_primes:
                    return primes_list

            primes_list = primes_list[:1] # Reset primes_list

        primes_list = primes_list[:1] # Reset primes_list

    return None


while True:
    prime = next(primes)
    if test(prime):
        print prime
        print lst 
        break 



