#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Project Euler Problem #31
==========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""

# Answer: 73682

# Based on: https://andrew.neitsch.ca/publications/m496pres1.nb.pdf

# 1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

# list of coin deonominations
a = [1, 2, 5, 10, 20, 50, 100, 200] 

def f(n,k): # n is amount we're making change for, k is number of types of coin
	if k < 1 or n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return f(n, k-1) + f(n - a[k-1], k)

print f(200, 8)
