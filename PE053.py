"""
Project Euler Problem #53
==========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^5C[3] = 10.

In general,

^nC[r] =   n!    ,where r n, n! = n * (n1) * ... * 3 * 2 * 1, and 0! = 1.
         r!(nr)!

It is not until n = 23, that a value exceeds one-million: ^23C[10] =
1144066.

How many values of  ^nC[r], for 1 n 100, are greater than one-million?
"""

from euler_functions import n_choose_k

total = 0
for n in xrange(1, 101):
    for k in xrange(1, n):
        if n_choose_k(n, k) > 1000000:
            total += 1

print total 


# And as a one liner:

print sum(n_choose_k(n, k) > 1000000 for n in xrange(1, 101) 
            for k in xrange(1, n) if n_choose_k(n, k) > 1000000)