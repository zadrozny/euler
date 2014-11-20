# PE067.py

import requests

t = requests.get('http://projecteuler.net/project/resources/p067_triangle.txt').text

t = list(reversed([map(int, line.split()) for line in t.split('\n')][:-1])) # Last row empty

for row_index, row in enumerate(t):
	for number_index, number in enumerate(row):
		try: 
			larger = max(number, row[number_index+1]) 	# Choose larger of neighbors
			t[row_index + 1][number_index] += larger 	# Add to row below (triangle is upside down)
		except IndexError:
			pass 

print t[-1][0]