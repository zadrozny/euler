#PE003.py
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143

x = 3 # Because n is odd, start with 3 and not 2

candidate = None	# Potential largest prime factor

while x <= n:
    if n % x == 0:
        candidate = x
        n = n / x # Update n to prevent redudancy
    x += 2 # Since all primes > 2 are odd

print candidate