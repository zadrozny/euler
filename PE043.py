"""
Project Euler Problem #43
==========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

num = '1406357289'

def test(n):
    divisors = [17, 13, 11, 7, 5, 3, 2]
    for i in range(1, 8):
        if int(n[i:i+3]) % divisors.pop() != 0:
            return False
    return True	

members = [int(''.join(candidate)) for candidate in 
             permutations(num) if test(''.join(candidate))]

print sum(members)