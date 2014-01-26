#PE12.py
'''
What is the value of the first triangle number to have over five hundred divisors?
'''

def generateTriangle(trianglenum):
	return sum(range(trianglenum+1))


def getDivisors(n):
	divisors  = []
	candidate = 1
	multiple  = n/candidate
	while candidate <= multiple:			#== ensure squares are included
		if n%candidate == 0:
			divisors.extend([candidate, multiple])
		candidate += 1
	return len(list(set(divisors)))			#Set() removes duplicates from squares 


ordinal = 1
while True: 	
	triangle = generateTriangle(ordinal)
	divisors = getDivisors(triangle)
	if divisors > 500:
		print triangle
		break 
	ordinal += 1 