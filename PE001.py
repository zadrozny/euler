# PE001.py

'''Find the sum of all the multiples of 3 or 5 below 1000.'''

print sum(n for n in xrange(1000) if n % 3 == 0 or n % 5 == 0)

##############################################################

total = 0

for number in range(1000): 
    if number % 3 == 0 or number % 5 == 0:
        total = total + number 

print total 