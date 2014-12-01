#PE28.py
'''
What is the sum of the numbers on the diagonals in 
a 1001 by 1001 spiral...?
'''


prior_square = 1 # The center of the spiral
total = 1

for n in range(3, 1003, 2): # Only consider odd squares; so step = 2
    square = n**2

    # Distance from, eg, 3^2 to next new corner, ie, 13
    distance = (square - prior_square) / 4 

    # Add each new corner:
    total += (prior_square + 1*distance  + 
             (prior_square + 2*distance) + 
             (prior_square + 3*distance) + 
             (prior_square + 4*distance))

    prior_square = square

print total