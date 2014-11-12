'''
Cubic permutations
Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''


from collections import Counter 


class Candidate():
	def __init__(self, root):
		self.root = root
		self.cube = self.root**3
		self.count = Counter(str(self.cube))
		

root = 345
permutations = {}

while True:
	c = Candidate(root)

	hashed = str(sorted(str(c.cube)))

	if hashed not in permutations:
		permutations[hashed] = [c.cube]
	else:
		permutations[hashed].append(c.cube)

	if len(permutations[hashed]) == 5:
		print permutations[hashed]
		break 

	root+=1

