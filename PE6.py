#PE6.py
'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

#25164150

sumSquares = 0 
summation = 0

for n in range(1, 101):
    sumSquares += n**2 
    summation += summation + n 

squareSum = summation**2

difference = squareSum - sumSquares

print difference 

