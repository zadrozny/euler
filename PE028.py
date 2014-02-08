#PE28.py
'''
What is the sum of the numbers on the diagonals in 
a 1001 by 1001 spiral...?
'''

n      =  1             	#Starting number
total  =  1
step   =  2					#Increment
height =  width = 1001
last   =  width * height  	#Final number


while n < last:
	for x in range(4):  	#Four corners...
		n = n + step        #Diagonal number
		total += n
	step += 2				#Steps are multiples of 2


print total