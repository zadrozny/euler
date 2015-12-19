#!/usr/bin/python2
# -*- coding: utf-8 -*-

#PE12.py
'''
What is the value of the first triangle number to have over five hundred divisors?
'''

def divisors(n):
    if n == 1:
        return [1]

    divisors = []
    candidate = 1
    while candidate <= n / candidate:
        if n % candidate == 0:
            divisors.extend([candidate, n / candidate])
        candidate += 1

    return divisors


last = 1
triangle = 0
while True:
    triangle += last
    if len(divisors(triangle)) > 500:
        print triangle
        break 
    last += 1
