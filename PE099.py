"""
Project Euler Problem 99
========================

Comparing two numbers written in index form like 2^11 and 3^7 is not
difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the
greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""
from math import log
import requests

r = requests.get('https://projecteuler.net/project/resources/p099_base_exp.txt').text


# Create a list consisting of: line number (enumerating from 1), base, and exponent
f = [[i]+[int(n) for n in l.split(',')] for i, l in enumerate(r.split('\n'), 1)]

# Get the logarithm of each pair
# Sort the pairs by the size of the result
# Get the line number from the last line-base-exponent
print sorted(f, key=lambda t: t[2]*log(t[1], 10))[-1] 
