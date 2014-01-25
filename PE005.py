#PE5.py
#Note: Could be optimized
'''
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20? 
''' 

def find():											#Wrap in function to break out of loops
	upper_divisor = 20 
	lower_divisor = 11								#Skip dividing candidates by 1 - 10; implicit 
	candidate 	  = upper_divisor 

	while True:										#Check until found
	    current_divisor = lower_divisor 			

	    candidate += 20 							#Begin at 40 (could be optimized)
	     
	    while current_divisor < upper_divisor:
	        if candidate % current_divisor == 0:          
	            current_divisor += 1
	        else: 
	            break 								#Current divisor resets to lower_divisor
	        if current_divisor == upper_divisor:
	            return candidate 					#(And break out of inner and outer loop)

print find()
