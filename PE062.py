'''
Cubic permutations
Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

permutations = {}

root = 345

while True:
	cube = root**3

	perm_key = str(sorted(str(cube)))

	if perm_key not in permutations:
		permutations[perm_key] = [cube]
	else:
		permutations[perm_key].append(cube)

		if len(permutations[perm_key]) == 5: # 'exactly five permutations...'
			print permutations[perm_key][0]
			break 

	root+=1

