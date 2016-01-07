"""
Project Euler Problem #38
==========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import permutations

# The answer is a permutation of 987654321.
# We want to get as close to 987654321 as possible.
# 987654321 itself is impossible because "n > 1". 
# Start with the largest permutation and work downwards.

# We know that the example given, 918273645, is a possibility, and it is close to the largest theoretically possible number; therefore, we can eliminate all possibilities that are smaller.

search_space = [''.join(perm) for perm in list(permutations('987654321')) if int(''.join(perm)) >= 918273645]


def test_candidate(candidate):
    '''Check whether candidate pandigital is pandigital multiple.'''
	
    for i in range(len(candidate)):		
        multiplicand = int(candidate[:i+1])
        s = ""	# The concatenated result
        n = 1	# The multiplier range
        while len(s) < 9:  # Where 9 is all the digits
            s = s + str(multiplicand * n)
            n+=1

        n -= 1 #Correct for final n+=1
        if s == candidate and n > 1:
            return candidate
    else: 
        return None


for candidate in search_space:
    result = test_candidate(candidate)
    if result:
        print result
        break 

