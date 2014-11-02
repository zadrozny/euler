#PE30.py

def check(n):
	'''Returns True if a number is the sum of the fifth power of its digits'''
	if n == sum(int(x)**5 for x in str(n)):
		return True
	else: 
		return False

#The sum of all the numbers that can be written as 
#the sum of fifth powers of their digits.
print sum(n for n in range(2, 645705) if check(n))
