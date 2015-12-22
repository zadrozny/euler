""" 
Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_proper_divisors(n): 
    '''Return sum of proper divisors of n'''
    divisors = [1]            # Include 1 to optimize, exclude n

    i = 2
    while i <= n/i: 
        if n % i == 0: 
            divisors.extend([i, n/i])
        i += 1
     		
    return sum(set(divisors)) # Remove duplicates from squares, then sum


amicables = []

for n in range(2, 10000): 
    if n in amicables:
        pass
    else: 
        total = sum_proper_divisors(n)
        if n == sum_proper_divisors(total) and n != total: 
            amicables.extend([n, total])

print sum(amicables)
