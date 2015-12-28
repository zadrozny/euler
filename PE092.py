#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

cache = {} # Save already calculated chains

total = 0
for n in range(1, 10000000):
    origin = n # Copy starting number (will change below)
    while True:
    	# Check whether an element in subchain has been seen
        if n in cache:
            if cache[n] == 89:
                total += 1
                cache[origin] = 89
                break
            else:
                cache[origin] = 1
                break 
        
        # ...if not, add the squares of the digits        
        n = sum([int(d)**2 for d in list(str(n))])

        if n == 89:
            cache[origin] = n
            total += 1
            break
        elif n == 1:
            cache[origin] = n
            break

print total
