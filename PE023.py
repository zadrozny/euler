#PE23.py

"""
...By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers...

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers. 
"""

def find_proper_divisors(n):
    "Returns list of proper divisors of n."
    if n==1: 
        return []
    else:
        divisors = [1]
        i = 2
        while i <= n/i: 
            if n % i == 0: 
                divisors.append(i)
                if i != n/i: 
                    divisors.append(n/i) # Do not duplicate squares
            i+=1
        return divisors
		

def find_type(n):
    proper_divisors = find_proper_divisors(n)
    summation = sum(proper_divisors)
    number_type = ""
    if summation < n: 
        number_type = "deficient"
    elif summation == n: 
        number_type = "perfect"
    elif summation > n: 
        number_type = "abundant"
    return number_type


abundant_numbers = [] 
abundant_sums = []


def find_abundant_sums(n):
    abundant_numbers.append(n)
    for i in abundant_numbers:
        abundant_sums.append(i + n)


for n in range(1, 28123 + 1):
    if find_type(n) == "abundant": 
        find_abundant_sums(n)


print sum(set(range(1, 28123 + 1)) - set(abundant_sums))