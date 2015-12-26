#PE7.py
'''
What is the 10 001st prime number?
'''

prime_list = [2, 3] 

candidate = prime_list[-1]


while len(prime_list) < 10001:
    candidate += 2                    # Start at 5 and check only odds
    
    for prime in prime_list[1:]:      # Skip 2
        if candidate % prime == 0:    # Not a prime
        	break
    else: 
    	prime_list.append(candidate)


print prime_list[-1]
