#PE7.py
'''
What is the 10 001st prime number?
'''

primelist = [2, 3] 

candidate = primelist[-1]

while len(primelist)<10001:
    candidate += 2							#Start at 5 and check only odds
    
    append = True							#Prime until proven otherise

    for number in primelist[1:]:  			#Skip 2
        if candidate % number == 0:
        	append = False
        	break
        
    if append: 
    	primelist.append(candidate)

print primelist[-1]
