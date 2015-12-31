#PE30.py

# First we establish an upper bound for n
# concatenating 9's until the concatenated number is 
# larger than the sum of the fifth powers of its digits

n = 9 
while True:
	bound = sum(9**5 for char in str(n))
	if n > bound: 
		break 
	n = int(str(n)+str(9)) # Concatenate


# Then we find the sum of all the numbers that can be 
# written as the sum of fifth powers of their digits
# (As 1 = 1^4 is not a sum it is not included.)

print sum(n for n in range(2, bound) 
	         if n == sum(int(char)**5 for char in str(n))) 

