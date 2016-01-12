#PE25.py
"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

prior, current = 1, 1 # Initialize Fib
terms = 2             # ...with two terms

while True:
    terms += 1
    prior, current = current, prior + current
    if len(str(current)) == 1000: # digits
        print terms
        break
