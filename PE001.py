#PE 1: Find the sum of all the multiples of 3 or 5 below 1000.

x = 0

for n in range(0, 1000): 
    if n % 3 == 0 or n % 5 == 0:
        x = x + n 
        
print x 
