'''Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.'''

path = r'ProjectEulerProblem13.txt'			#Number on PE site

total = 0

with open(path) as f: 
	for line in f:
		total += int(line.strip('\n'))

print total 