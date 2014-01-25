#PE11.py 
""" 
What is the greatest product of four adjacent numbers in any
direction (up, down, left, right, or diagonally) in the 2020 grid?
"""

from numpy import prod


f = #Path to 20x20 grid

with open(f) as f: 
	matrix = [[int(n) for n in line.strip('\n').split()] for line in f]

height = width = len(matrix)		
seqLength = 4									#Four adjacent numbers


def sum_east(y, x):
	if x <= len(matrix[y]) - seqLength:
		return prod(matrix[y][x:x+seqLength])


def sum_south(y, x): 
	if y <= len(matrix) - seqLength: 
		return prod([r[y] for r in matrix[x:x+4]])


def sum_southeast(y, x): 
	if x <= len(matrix[y]) - seqLength and y <= len(matrix) - seqLength:
		return prod([matrix[y+i][x+i] for i in range(seqLength)])


def sum_southwest(y, x): 
	if x >= seqLength - 1 and y <= len(matrix) - seqLength: 
		return prod( [matrix[y+i][x-i] for i in range(seqLength)] )


candidate = 0

for y in range(height):
	for x in range(width):
		e 		  = sum_east(y, x)
		s 		  = sum_south(y, x)
		se 		  = sum_southeast(y, x)
		sw  	  = sum_southwest(y, x)
		current   = max(e, s, se, sw)

		if current > candidate: 
			candidate = current


print candidate