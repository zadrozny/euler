#!/usr/bin/python2
# -*- coding: utf-8 -*-
#PE11.py 
""" 
What is the greatest product of four adjacent numbers in any
direction (up, down, left, right, or diagonally) in the 2020 grid?
"""

from numpy import prod

f = "PE011number.txt"

with open(f) as f: 
	m = [[int(n) for n in line.strip('\n').split()] for line in f]


best = 0
for y in range(len(m)):        # Top to bottom
    for x in range(len(m[y])): # ...and left to right
        
        right = prod(m[y][x:x+4]) # Obviates left, some redundancy
        
        try:
            down = prod([m[y][x+i] for i in range(4)]) # Obviates up
        except IndexError:
            pass

        try:
            diagonal_down = prod([m[y+i][x+i] for i in range(4)])
        except IndexError:
            pass

        try:
            diagonal_up  = prod([m[y-i][x+i] for i in range(4)])
        except IndexError:
            pass

        best = max(best, max(right, down, diagonal_down, diagonal_up))

print best        