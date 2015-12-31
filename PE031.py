#!/usr/bin/python
# -*- coding: utf-8 -*-

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

# list of coin denominations
denominations = [1, 2, 5, 10, 20, 50, 100, 200] 


def make_change(amount, coin_types): 
    if coin_types < 1 or amount < 0:
        return 0
    elif amount == 0:
        return 1
    else:
        return make_change(amount, coin_types-1) + \
               make_change(amount - denominations[coin_types-1], coin_types)

print make_change(200, 8)
