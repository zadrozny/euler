# PE067.py

import requests

t = requests.get('http://projecteuler.net/project/resources/p067_triangle.txt').text

t = [map(int, line.split()) 
		for line in t.split('\n')][:-1] # Remove empty last row


first = t[0] # The top of the triangle
previous_row = [0] * len(t[-1]) # Initialize a fake previous row of zeros.


for row in reversed(t[1:]):

	row = map(sum, zip(previous_row, row)) # First iteration with fake.
	
	# Keep larger of two neighbors in row:
	row = [max(row[i], row[i+1]) for i, n in enumerate(row[:-1])]

	previous_row = row # Update with real previous rows.


print previous_row[0] + first[0] 

