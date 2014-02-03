'''Find the sum of the digits in the number 100!'''

import math

print sum([int(digit) for digit in str(math.factorial(100))])