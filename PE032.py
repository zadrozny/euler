"""
Project Euler Problem #32
==========================

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""


from itertools import permutations

perms = list(permutations('123456789'))

products = []
for perm in perms:
	perm = list(perm)
	for x in range(1, 8):
		perm_copy = perm[:]		  #Prevent duplication of '*', eg, '**' and '***'
		perm_copy.insert(x, '*')
		for y in range(x+2, 8):
			candidate = perm_copy[:]
			candidate.insert(y, '==')
			candidate = ''.join(candidate)
			if eval(candidate): #If idenity is true...
				products.append(int(candidate.split("==")[1]))

products = list(set(products)) #Remove duplicate products

print sum(products)