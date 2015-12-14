#PE5.py
#Note: Could be optimized. Brute force but very readable. 
'''
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20? 
''' 

divisors = range(11, 20) # Divisors 1 - 10 implicit
candidate = 20
while True:
    for d in divisors:
        if candidate % d != 0:
            candidate += 20
            break 
    else:
        print candidate
        break 
