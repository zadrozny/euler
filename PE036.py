"""
Project Euler Problem #36
==========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""



total = 0
for n in range(1000000):
	if list(str(n)) == list(reversed(str(n))):
		b = bin(n)[2:]
		if list(b) == list(reversed(b)):
			total += n

print total 