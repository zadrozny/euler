#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find():
    for a in range(1, 999):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

print find()                
