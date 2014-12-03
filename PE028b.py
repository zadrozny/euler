#PE28b.py A simpler implementation: generate and sum the sequence.

'''
What is the sum of the numbers on the diagonals in 
a 1001 by 1001 spiral...?
'''


n = 1
total = 1 
increment = 2
while n < 1001**2:
	for i in range(1, 5): # Four corners
		n += increment 
		total += n 
	increment += 2 # Sides alway grow by two

print total 	