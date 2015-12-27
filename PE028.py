#PE28.py
'''
What is the sum of the numbers on the diagonals in 
a 1001 by 1001 spiral...?
'''

total = 1 # The center of the spiral

# Start is 3 because we already have spiral center
# Stop is the dimension of the square: 1001
# Step is 2 because the 1001 is odd
for i in range(3, 1001 + 1, 2):
    # Start is the upper right corner
    # Stop is the lower right corner
    # Step is negative because we're spirling backwards / counter-clockwise
    total += sum(range(i**2, i**2 - 4*(i-1), -1*(i-1)))

print total
