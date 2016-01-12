#!/usr/bin/python2
# -*- coding: utf-8 -*-

from collections import Counter


def prime_factors(n):
    factors = []

    p = 2
    while n % p == 0:
        factors.append(p)
        n = n / p
        
    p = 3
    while p <= n:
        while n % p == 0:
            factors.append(p)
            n = n / p
        p += 2 

    return factors


result = Counter()
for n in range(11, 21):
    factors = prime_factors(n)
    for f in set(factors):
        if factors.count(f) > result[f]:
            result[f] = factors.count(f)


print reduce(lambda x, y: x*y, [k**v for k,v in result.items()])

