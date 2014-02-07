#PE25.py
"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

termLength = 1000


#Solution one: more memory intensive, possibly clearer
fibs = [1, 1]
while True:
	fibs.append(fibs[-1] + fibs[-2])
	if len(str(fibs[-1])) == termLength:
		print len(fibs)
		break 


#Solution two: less memory intensive, possibly more opaque
prior, current = 1, 1
terms = 2
while True:
	terms += 1
	prior, current = current, prior + current
	if len(str(current)) == termLength:
		print terms
		break
		 