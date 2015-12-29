#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
'''

import requests

r = requests.get('https://projecteuler.net/project/resources/p081_matrix.txt').text

M = [[int(n) for n in l.split(',')] for l in r.strip('\n').split('\n')]


# Iterate over each cell in the Matrix
# Choose smaller of two paths (left or above) and update
for y, r in enumerate(M):
    for x, c in enumerate(r):
        left = M[y][x-1] if x > 0 else None
        above = M[y-1][x] if y > 0 else None
        if left and above:
            M[y][x] = min(left, above) + M[y][x]
        elif left:
            M[y][x] = left + M[y][x]
        elif above:
            M[y][x] = above + M[y][x]

print M[79][79] # Last cell, after updating
