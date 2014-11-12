'''
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (4053). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

permutations = {}

root = 345 # The cube's root must be larger than 345

while True:
	cube = root**3

	permutation_key = str(sorted(str(cube)))

	if permutation_key not in permutations:
		permutations[permutation_key] = [cube]
	else:
		permutations[permutation_key].append(cube)

		if len(permutations[permutation_key]) == 5: # 'exactly five permutations'
			print permutations[permutation_key][0]
			break 

	root+=1

