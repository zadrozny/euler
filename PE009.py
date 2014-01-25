#PE9.py
"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def findTriplet():
	a = 1
	b = 1
	while a < 999:
	    
	    bplusc = 1000 - a   
	      
	    while b < bplusc:
	        
	        c = bplusc - b 
	              
	        if a*a + b*b == c*c:
	            return 	str(a) + ' plus '   +	\
	            	    str(b) + ' plus '   +	\
	            		str(c) + ' equals '	+	\
	            		str(a+b+c)
	             
	        b += 1
	        
	    b = 1    
	    a += 1

print findTriplet()
