#from __future__  import division
from operator import mul
from itertools import combinations


def factorial(n):
    '''Return the factorial of a number.'''

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be an integer >= 0.")

    return 1 if n == 0 else reduce(lambda x, y: x*y, (range(1, n+1)))



def get_prime_factors(n):
    '''Return prime factors of a number.'''

    if n <= 0:
		raise ValueError("n must be greater than 0.")

    if n % 2 == 0:
        prime_factors = [2]

    else:
        prime_factors = []


    divisor = 3  # Skip 2, so increments can be odd

    while divisor <= n:
        if n % divisor == 0: 
            prime_factors.append(divisor)

            n = n / divisor  			  # Update n to prevent redundancy

            if n % divisor == 0:		  # Remove powers of a number
                while n % divisor == 0:
                    n = n / divisor

        divisor += 2  # All primes > 2 are odd

    return prime_factors



def list_first_n_primes(n):
    '''Return a list of n primes'''

    if n == 0:
        return []

    if n == 1:
        return [2]

    if n == 2:
        return [2, 3]

    prime_list = [2, 3]  # Intialize with 2 to skip evens.

    candidate = 5	
    while len(prime_list) < n:
        for prime in prime_list:			
            if candidate % prime == 0:	# It's not prime.
                break	
            if prime > candidate / prime: # It is prime.
                prime_list.append(candidate) 	
                break
        candidate += 2	# Skip evens.			
				
    return prime_list


def generate_primes_less_than(n):
    '''Return a list of primes less than n.'''

    if n <= 2: return []

    if n == 3: return [2]
    
    if n <= 5: return [2, 3]

    prime_list = [2, 3] # Intialize with 2 to skip evens

    for candidate in xrange(5, n, 2):       # Skip evens
        for prime in prime_list:            
            if candidate % prime == 0:      # It's not prime
                break   
            if prime > candidate / prime:   # It is prime
                prime_list.append(candidate)    
                break   
            
    return prime_list


def generate_next_prime(start=0, stop=None):
    '''
    Yield the next prime, ad infinitum; 
    or yield primes within the limits start and stop.
    '''

    if start != 0:
        prime_list = generate_primes_less_than(start+1)
    else: 
        prime_list = [] 					

    if len(prime_list) == 0:
        prime_list.append(2)
        yield 2
    if len(prime_list) == 1:
        prime_list.append(3)
        yield 3

    candidate = prime_list[-1]  # Strictly speaking this is a prime, not candidate.

    while stop is None or candidate <= stop: 
        candidate += 2	# Skip evens; evaluate the next odd number.
        for prime in prime_list:			
            if candidate % prime == 0:	 # It's not prime.
                break	
            if prime > candidate / prime: # It is prime.
                prime_list.append(candidate)
                yield candidate 	
                break



def generate_triangle_number(n):
    '''Returns the triangle T of n. Equivalent to sum(range(n+1)).'''
    return (n*(n+1))/2

    
def is_prime(candidate):
    '''Return True if prime and False if not.'''

    if candidate <= 0:
        raise ValueError("Integer must be > 0; you entered: ", candidate)

    if candidate == 1: 
        return False 
		
    if candidate == 2:
        return True
	
    if candidate == 3:
        return True

    if candidate % 2 == 0:
        return False

    divisor = 3
    while divisor <= candidate / divisor:
        if candidate % divisor == 0:
            return False
        divisor += 2

    return True 



def multiply(lst):
    '''Return the product of a list.'''

    if type(lst) != list:
        raise Exception("You need a list. You entered a: ", type(lst))

    product = 1 
    for term in lst:
        product *= term

    return product 



def n_choose_k(n, k):
    '''Return k combinations n elements: n! / k!*(n-k)!'''

    return factorial(n) / (factorial(k) * factorial(n - k))

