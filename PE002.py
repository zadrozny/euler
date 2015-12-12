# PE002.py 
'''
By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

total = 0 

prior, current = 1, 2

while current <= 4000000:
    if current % 2 == 0:
        total += current
    prior, current = current, prior + current

print total      
